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


FREQUENCY_CHOICES = [
    ("DAILY", "every day"),
    ("WEEKLY", "every week"),
    ("MONTHLY", "every_month"),
]

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
    name = models.CharField(max_length=255, verbose_name='Название рассылки')
    message = models.ForeignKey(Message, verbose_name='Сообщение', related_name='mailings', **CASCADE)
    clients = models.ManyToManyField(Client, verbose_name='Клиенты', related_name='mailings')
    user = models.ForeignKey(User, verbose_name='Создатель', related_name='mailings', **CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    first_attempt_at = models.DateTimeField(verbose_name='Дата и время первой рассылки', **NULL)
    last_attempt_at = models.DateTimeField(verbose_name='Дата и время последней попытки', **NULL)
    started_at = models.DateTimeField(verbose_name='Дата и время начала')
    completed_at = models.DateTimeField(verbose_name='Дата и время завершения')

    sending_interval = RelativeDeltaField(verbose_name='Интервал рассылки', **NULL)

    frequency = models.CharField(max_length=8, choices=FREQUENCY_CHOICES, verbose_name="Частота", default="DAILY")
    status = models.CharField(max_length=16, default="CREATED", choices=MAILING_STATUS_CHOICES, verbose_name="Статус")

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f"Рассылка {self.pk}"

    def set_sending_interval(self):
        if self.frequency == "DAILY":
            self.sending_interval = relativedelta(days=1)
        elif self.frequency == "WEEKLY":
            self.sending_interval = relativedelta(weeks=1)
        elif self.frequency == "MONTHLY":
            self.sending_interval = relativedelta(months=1)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.set_sending_interval()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    def try_n_attempts(self, now, n=10):
        sent = False
        attempts = []
        for i in range(n):
            try:
                response = send_mail(self.message.subject, self.message.body, None, recipient_list=self.clients.values_list('email', flat=True),
                                     fail_silently=False)
            except SMTPException as e:
                response = str(e)
                status = "FAILED"
            else:
                status = "OK"
                sent = True

            attempts.append(MailingAttempt(mailing=self, attempt_at=now, status=status,
                                           server_response=response))
            if sent:
                return attempts
        return attempts


class MailingAttempt(models.Model):
    mailing = models.ForeignKey(Mailing, verbose_name='Рассылка', related_name='attempts', **SET_NULL, **NULL)
    attempt_at = models.DateTimeField(verbose_name='Дата и время попытки', **NULL)
    status = models.CharField(max_length=6, choices=ATTEMPT_STATUS_CHOICES, verbose_name="Статус")
    server_response = models.CharField(max_length=128, verbose_name="Ответ почтового сервера", **NULL)
