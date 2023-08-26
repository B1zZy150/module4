# Generated by Django 4.2.3 on 2023-08-26 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_advertisment', '0002_alter_advertisement_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='auction',
            field=models.BooleanField(help_text='Отьметьте, если торг уместен', verbose_name='Торг'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='created_ad',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='updated_ad',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время редактирования'),
        ),
    ]