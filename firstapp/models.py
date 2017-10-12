from django.db import models

# Create your models here.
class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет-адрес пиццерии')

    class Meta:
        verbose_name='Пиццерия'
        verbose_name_plural='Пиццерии'

    # в данной реализации функция меняет название объекта на сайте
    def __str__(self):
        return self.name

class Pizza(models.Model):
    pizza_shop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    photo = models.ImageField('Фото', upload_to='firstapp/photos', default='', blank=True)

    class Meta:
        verbose_name='Пицца'
        verbose_name_plural='Пиццы'
        ordering = ['name']

    # в данной реализации функция меняет название объекта на сайте
    def __str__(self):
        return self.name

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, verbose_name='Пицца')
    name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.CharField(max_length=30, verbose_name='Телефон')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
