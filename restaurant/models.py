from cgitb import text
from django.db import models

class CategoryMenu(models.Model):
    name = models.CharField(verbose_name='Названия', max_length = 150)
    slug = models.SlugField(max_length = 150, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню ресторана'
        verbose_name_plural = 'Меню ресторана'


class RangeMenu(models.Model):
    title = models.CharField(verbose_name='Названия', max_length = 150)
    image = models.ImageField(verbose_name='Изображение', upload_to='images_menu/')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(verbose_name='Цена', max_digits=5, decimal_places=2, default='')
    category_menu = models.ForeignKey(CategoryMenu, verbose_name='Меню ресторана', on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 150, unique=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Ассортимент меню ресторана'
        verbose_name_plural = 'Ассортимент меню ресторана'