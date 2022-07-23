from django.db import models
from django.urls import reverse

class OurAddress(models.Model):
    address = models.CharField(verbose_name='Адрес', max_length=150)
    phone = models.CharField(verbose_name='Телефон', max_length=150)
    email = models.EmailField(verbose_name='Email', max_length=254)
    website = models.URLField(verbose_name='URL', max_length=200)
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'Наши данные'
        verbose_name_plural = 'Наши данные'


