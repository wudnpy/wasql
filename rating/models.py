from django.db import models

# Create your models here.
class DescriptionData(models.Model):
    d_group = models.IntegerField()
    d_pokazatel = models.IntegerField()
    d_score = models.IntegerField() # типы фильтров в форме: 0 - без фильтров, 1 - с вводом данных в текстовое поле, 2 - с выбором даты начала и конца периода.

    def __str__(self):
        return self.d_pokazatel
