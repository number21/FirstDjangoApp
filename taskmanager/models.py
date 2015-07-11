from django.db import models

# Create your models here.
class Task(models.Model):

    class Meta(object):
        verbose_name = u"Завдання"
        verbose_name_plural = u"Завдання"

    task_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва завдання")

    customer_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім'я замовника")

    start_date = models.DateField(
        blank=True,
        verbose_name=u"Дата початку",
        null=True)

    end_date = models.DateField(
        blank=False,
        verbose_name=u"Дата початку",
        null=True)
    status = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Статус")

    picture = models.ImageField(
        blank=True,
        verbose_name=u"Фото",
        null=True)
    def __unicode__(self):
        return "{} {}".format(self.task_name, self.customer_name)