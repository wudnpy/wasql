from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=100)
    total_time = models.IntegerField(default=0)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Запрос'
        verbose_name_plural='Запросы'
        ordering = ['number']
