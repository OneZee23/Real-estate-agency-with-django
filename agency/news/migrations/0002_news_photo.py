# Generated by Django 3.1.7 on 2021-05-15 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='photo',
            field=models.ImageField(default='photos/2021/03/14/home-1.jpg', upload_to='news/photos/%Y/%m/%d/', verbose_name='Обложка'),
        ),
    ]