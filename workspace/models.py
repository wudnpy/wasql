from django.db import models


# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100)
    total_time = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    q_type = models.IntegerField(default=0) # типы фильтров в форме: 0 - без фильтров, 1 - с вводом данных в текстовое поле, 2 - с выбором даты начала и конца периода.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Запрос'
        verbose_name_plural='Запросы'
        ordering = ['number']
