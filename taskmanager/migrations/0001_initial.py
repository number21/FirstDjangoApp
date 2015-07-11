# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('task_name', models.CharField(verbose_name='Назва завдання', max_length=256)),
                ('customer_name', models.CharField(verbose_name="Ім'я замовника", max_length=256)),
                ('start_date', models.DateField(verbose_name='Дата початку', blank=True, null=True)),
                ('end_date', models.DateField(null=True, verbose_name='Дата початку')),
                ('status', models.CharField(verbose_name='Статус', max_length=256)),
                ('picture', models.ImageField(verbose_name='Фото', upload_to='', blank=True, null=True)),
            ],
        ),
    ]
