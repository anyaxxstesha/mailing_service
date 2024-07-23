from django.db import models

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
    subject = models.CharField(max_length=256, **NULL, verbose_name='Тема письма')
    body = models.TextField(**NULL, verbose_name='Тело письма')
    user = models.ForeignKey(User, **CASCADE, verbose_name='Создатель письма')

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.subject

