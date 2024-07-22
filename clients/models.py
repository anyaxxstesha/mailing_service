from django.db import models


class Client(models.Model):
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

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["id"]

    def __str__(self):
        return self.email
