from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='department') # models.CASCADE отвечает за удалени связанных записей
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='department_logo/', blank=False)

    def __str__(self):
        return self.name
