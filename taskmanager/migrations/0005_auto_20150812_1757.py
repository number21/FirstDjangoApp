# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0004_auto_20150812_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=15, default='В процесі', choices=[('Готово', 'Готово'), ('В процесі', 'В процесі'), ('Прийнято', 'Прийнято')]),
        ),
    ]
