from django.db import models
from datetime import datetime


class News(models.Model):
  title = models.CharField("Название", max_length=200)
  photo = models.ImageField("Обложка", upload_to='news/photos/%Y/%m/%d/', default='photos/2021/03/14/home-1.jpg')
  text = models.TextField("Текст новости")
  author_name = models.CharField("ФИО", max_length=200)
  created_at = models.DateTimeField("Дата создания", default=datetime.now)
  updated_at = models.DateTimeField("Дата обновления", default=datetime.now)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'
    ordering = ['created_at', 'title']
