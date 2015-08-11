#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Task(models.Model):

    class Meta(object):
        verbose_name = u"Завдання"
        verbose_name_plural = u"Завдання"

    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва завдання")

    customer = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я замовника")

    date_start = models.DateField(
        blank=True,
        verbose_name=u"Дата початку",
        null=True)

    date_end = models.DateField(
        blank=False,
        verbose_name=u"Дата кінця",
        null=True)
    status = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Статус")

    picture = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)

    def __str__(self):
        return "{} {}".format(self.name, self.customer)