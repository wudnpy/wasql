from django.db import models

# Create your models here.
class Indicators(models.Model):
    group = models.CharField(max_length=255)
    indicator = models.TextField()
    calculation = models.CharField(max_length=255) # типы фильтров в форме: 0 - без фильтров, 1 - с вводом данных в текстовое поле, 2 - с выбором даты начала и конца периода.

    def __str__(self):
        return self.indicator
