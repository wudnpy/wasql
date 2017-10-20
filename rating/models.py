from django.db import models

# Create your models here.
class Indicators(models.Model):
    group = models.CharField(max_length=255)
    indicator = models.TextField()
    calculation = models.CharField(max_length=255)

    def __str__(self):
        return self.indicator

class Ac(models.Model):
    ac_name = models.CharField(max_length=80)

    def __str__(self):
        return self.ac_name
