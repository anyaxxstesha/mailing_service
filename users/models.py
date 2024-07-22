from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='email address'
    )

    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Имя',
        help_text='Введите имя'
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='Фамилия',
        help_text='Введите фамилию'
    )
    phone = models.CharField(
        max_length=35,
        verbose_name='Номер телефона',
        blank=True, null=True,
        help_text='Введите номер телефона в формате +7 (XXX)')
    company = models.CharField(
        max_length=100,
        verbose_name='Компания',
        blank=True, null=True,
        help_text='Укажите компанию'
    )
    avatar = models.ImageField(
        upload_to='users/avatars/',
        verbose_name='Аватар',
        blank=True, null=True,
        help_text='Загрузите аватар'
    )

    token = models.CharField(
        max_length=100,
        verbose_name='Токен',
        blank=True, null=True,
        help_text='Токен для входа в систему'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']

    def __str__(self):
        return self.email
