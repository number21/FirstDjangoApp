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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Назва завдання', max_length=256)),
                ('customer', models.CharField(verbose_name="Ім'я замовника", max_length=256)),
                ('date_start', models.DateField(verbose_name='Дата початку', null=True, blank=True)),
                ('date_end', models.DateField(verbose_name='Дата кінця', null=True)),
                ('status', models.CharField(verbose_name='Статус', choices=[('Готово', 'Готово'), ('Відкрите', 'Відкрите'), ('Прийнято', 'Прийнято')], default='Відкрите', max_length=15)),
                ('picture', models.ImageField(verbose_name='Зображення', upload_to='', null=True, blank=True)),
                ('description', models.TextField(verbose_name='Опис', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Завдання',
                'verbose_name': 'Завдання',
            },
        ),
    ]
