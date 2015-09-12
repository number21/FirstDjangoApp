#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from markdown import markdown
import bleach
import hashlib
from datetime import datetime


class Task(models.Model):

    class Meta(object):
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"

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

    PS = "Готово"
    IP = "Відкрите"
    AG = "Прийнято"
    STATUS_CHOICES = (
        (PS, 'Готово'),
        (IP, 'Відкрите'),
        (AG, 'Прийнято'))
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default=IP,
        verbose_name=u"Статус")
    picture = models.ImageField(
        blank=True,
        verbose_name=u"Зображення",
        null=True)
    description = models.TextField(
        blank=True,
        verbose_name=u"Опис")
    html_description = models.TextField(
        blank=True,
        editable=False)
    user = models.ForeignKey(User, default=1)
    creation_date = models.DateTimeField(
        blank=True,
        default=datetime.now)

    # TODO: Додати завантаження декількох картинок
    #     (Або картинки в поле опису задачі)

    def __str__(self):
        return "{} {}".format(self.name, self.customer)

    def save(self):
        self.html_description = bleach.clean(markdown(self.description))
        super(Task, self).save()


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def gravatar_url(self):
        return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
