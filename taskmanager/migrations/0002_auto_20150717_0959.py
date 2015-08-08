# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name_plural': 'Завдання', 'verbose_name': 'Завдання'},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='customer_name',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='end_date',
            new_name='date_end',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='start_date',
            new_name='date_start',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='task_name',
            new_name='name',
        ),
    ]
