from django.db import models
from datetime import datetime


class Realtor(models.Model):
  name = models.CharField("Имя", max_length=200)
  photo = models.ImageField("Фото", upload_to='photos/%Y/%m/%d/')
  description = models.TextField("Описание", null=True, blank=True)
  phone = models.CharField("Телефон", max_length=200)
  email = models.CharField("Электронная почта", max_length=200)
  is_mvp = models.BooleanField("Лучший работник месяца?", default=False)
  hire_date = models.DateTimeField("Дата найма", default=datetime.now, null=True, blank=True)

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = 'Риэлтор'
    verbose_name_plural = 'Риэлторы'
    ordering = ['hire_date', 'name']
