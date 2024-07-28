from django.db import models

from users.models import User


class Client(models.Model):
    """
    Model describing client (recipient) of the mailing
    """
    email = models.EmailField(
        unique=True,
        verbose_name='email address'
    )
    surname = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        help_text="Укажите фамилию",
    )
    name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Укажите имя",
    )
    patronymic = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        help_text="Укажите отчество",
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Добавьте комментарий",
        blank=True,
        null=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь, добавивший клиента')

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["id"]
        unique_together = ["email", "user"]

    def __str__(self):
        return self.email
