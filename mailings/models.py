from smtplib import SMTPException
from datetime import timedelta

from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from relativedeltafield import RelativeDeltaField
from dateutil.relativedelta import relativedelta

from clients.models import Client
from users.models import User

NULL = dict(
    null=True,
    blank=True
)

CASCADE = dict(
    on_delete=models.CASCADE
)

SET_NULL = dict(
    on_delete=models.SET_NULL
)


class Message(models.Model):
    subject = models.CharField(max_length=256, verbose_name='Тема письма', **NULL)
    body = models.TextField(verbose_name='Тело письма', **NULL)
    user = models.ForeignKey(User, verbose_name='Создатель письма', **CASCADE)

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.subject


class FrequencyChoices(relativedelta, models.Choices):
    DAILY = relativedelta(days=1), 'Daily'
    WEEKLY = relativedelta(weeks=1), 'Weekly'
    MONTHLY = relativedelta(months=1), 'Monthly'


MAILING_STATUS_CHOICES = [
    ("CREATED", "создана"),
    ("SENDING", "запущена"),
    ("COMPLETED", "завершена"),
]

ATTEMPT_STATUS_CHOICES = [
    ("OK", "успешно"),
    ("FAILED", "не успешно"),
]


class Mailing(models.Model):
    message = models.ForeignKey(Message, verbose_name='Сообщение', related_name='mailings', **CASCADE)
    clients = models.ManyToManyField(Client, verbose_name_plural='Клиенты', related_name='mailings')
    user = models.ForeignKey(User, verbose_name='Создатель', related_name='mailings', **CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    first_attempt_at = models.DateTimeField(verbose_name='Дата и время первой попытки', **NULL)
    last_attempt_at = models.DateTimeField(verbose_name='Дата и время последней попытки', **NULL)
    started_at = models.DateTimeField(verbose_name='Дата и время начала')
    completed_at = models.DateTimeField(verbose_name='Дата и время завершения')

    frequency = models.CharField(max_length=8, choices=FrequencyChoices, verbose_name="Частота", default="DAILY")
    status = models.CharField(max_length=16, default="CREATED", choices=MAILING_STATUS_CHOICES, verbose_name="Статус")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f"Рассылка {self.pk}"

    def try_n_attempts(self, n=10):
        sent = False
        attempts = []
        for i in range(n):
            try:
                response = send_mail(self.message.subject, self.message.body, None, recipient_list=[self.clients],
                                     fail_silently=False)
            except SMTPException as e:
                response = str(e)
                status = "FAILED"
            else:
                status = "OK"
                sent = True

            attempts.append(MailingAttempt(mailing=self, attempt_at=timezone.now(), status=status,
                                           server_response=response))
            if sent:
                return attempts
        return attempts


class MailingAttempt(models.Model):
    mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', related_name='attempts', **SET_NULL, **NULL)
    attempt_at = models.DateTimeField(verbose_name='Дата и время попытки', **NULL)
    status = models.CharField(max_length=6, choices=ATTEMPT_STATUS_CHOICES, verbose_name="Статус")
    server_response = models.CharField(max_length=128, verbose_name="Ответ почтового сервера", **NULL)
