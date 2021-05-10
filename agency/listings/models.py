from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  street = models.CharField("Улица", max_length=200)
  floor = models.IntegerField("Этаж")
  city = models.CharField("Город", max_length=200)
  district = models.CharField("Район", max_length=200)
  house_number = models.CharField("Номер дома", max_length=200)
  price = models.IntegerField("Цена")
  total_area = models.IntegerField("Общая площадь в м^2")
  rooms_number = models.IntegerField("Количество комнат", default=1)
  balcony = models.BooleanField("Наличие балкона", default=False)
  floors_number = models.IntegerField("Этажность дома", null=True, blank=True)
  ceiling_height = models.FloatField("Высота потолков", null=True, blank=True)
  kitchen_area = models.IntegerField("Площадь кухни", null=True, blank=True)
  residental_area = models.IntegerField("Площадь жилая", null=True, blank=True)
  material = models.CharField("Материал дома", max_length=200, null=True, blank=True)
  year_construction = models.IntegerField("Год постройки дома", null=True, blank=True)
  company_construction = models.CharField("Строительная компания", max_length=200, null=True, blank=True)
  photo_main = models.ImageField("Главное фото", upload_to='photos/%Y/%m/%d/')
  photo_1 = models.ImageField("Фото 1", upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  photo_2 = models.ImageField("Фото 2", upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  photo_3 = models.ImageField("Фото 3", upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  photo_4 = models.ImageField("Фото 4", upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  photo_5 = models.ImageField("Фото 5", upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  photo_6 = models.ImageField("Фото 6", upload_to='photos/%Y/%m/%d/', null=True, blank=True)
  is_published = models.BooleanField("Выставлен на продажу", default=True)
  list_date = models.DateTimeField("Дата", default=datetime.now, null=True, blank=True)

  def __str__(self):
    return self.street
