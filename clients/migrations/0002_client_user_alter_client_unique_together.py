# Generated by Django 4.2.2 on 2024-07-28 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь, добавивший клиента'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together={('email', 'user')},
        ),
    ]
