# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_auto_20150812_1757'),
    ]

    operations = [
        migrations.DeleteModel(
            name='State',
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=15, default='Відкрите', choices=[('Готово', 'Готово'), ('Відкрите', 'Відкрите'), ('Прийнято', 'Прийнято')]),
        ),
    ]
