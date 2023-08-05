from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone


class Advertisement(models.Model):
    title =  models.CharField('Заголовок', max_length=128, )
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг',help_text='Отьметьте, если торг уместен')
    created_ad = models.DateTimeField('Дата и время создания',auto_now_add=True)
    updated_ad = models.DateTimeField('Дата и время редактирования',auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_ad.date() == timezone.now().date():
            created_time = self.created_ad.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: green; font-weight: bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_ad.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата редактирования')
    def updated_date(self):
        if self.updated_ad.date() == timezone.now().date():
            created_time = self.updated_ad.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color: blue; font-weight: bold;"> Сегодня в {} </span>', created_time
            )
        return self.created_ad.strftime('%d.%m.%Y в %H:%M:%S')

    def __str__(self):
        return f'Advertisement (id = {self.id}, title = {self.title}, price = {self.price})'
 
    class Meta:
       db_table = 'Advertisement'

    