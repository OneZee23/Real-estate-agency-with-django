from django.db import models
from datetime import datetime


class Contact(models.Model):
  listing = models.CharField("Недвижимость", max_length=200)
  listing_id = models.IntegerField("ID недвижимости")
  name = models.CharField("ФИО", max_length=200)
  email = models.CharField("Электронная почта", max_length=100)
  phone = models.CharField("Телефон", max_length=100)
  message = models.TextField("Сообщение", blank=True)
  contact_date = models.DateTimeField("Дата заявки", default=datetime.now, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Заявки пользователя'
    verbose_name_plural = 'Заявки пользователей'
    ordering = ['contact_date', 'listing']
