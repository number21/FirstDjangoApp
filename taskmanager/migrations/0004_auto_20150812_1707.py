# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0003_auto_20150808_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('status', models.CharField(max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статус',
            },
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(to='taskmanager.State', on_delete=django.db.models.deletion.PROTECT, null=True, verbose_name='Статус'),
        ),
    ]
