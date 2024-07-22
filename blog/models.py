from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Наименование поста",
        help_text="Укажите название поста",
    )
    content = models.TextField(
        verbose_name="Текст поста",
        help_text="Добавьте текст поста",
        blank=True,
        null=True,
    )
    preview_image = models.ImageField(
        upload_to="blog/images",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите изображение для поста",
    )
    created_at = models.DateField(
        auto_now_add=True,
        verbose_name="Дата создания поста",
        help_text="Генерируется автоматически",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Маркер публикации/архивации поста",
        help_text="Укажите, будет ли пост опубликован",
    )
    views_amount = models.PositiveIntegerField(
        default=0,
        verbose_name="Просмотры"
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["created_at"]

    def __str__(self):
        return self.title
