# Generated by Django 3.1.7 on 2021-03-21 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20210314_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='rooms_number',
            field=models.IntegerField(default=1, verbose_name='Количество комнат'),
        ),
    ]
