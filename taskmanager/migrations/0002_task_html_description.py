# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='html_description',
            field=models.TextField(editable=False, blank=True),
        ),
    ]
