from django.db import models



class About(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    video = models.FileField(verbose_name='Видео', upload_to='video/') 
    image = models.ImageField(verbose_name='Изображение', upload_to='image/', blank=True, null=True)
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'
    


class Customer(models.Model):
    customer_about = models.CharField(verbose_name='Заголовок', max_length=150)
    custom_says = models.TextField(verbose_name='О чём мы говорим')

    
    def __str__(self):
        return self.customer_about
    
    class Meta:
        verbose_name = 'О персонале'
        verbose_name_plural = 'О персонале'

class CustomerPerson(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    photo_person = models.ImageField(verbose_name='Фото персонала', upload_to='photo_person')
    info_person = models.TextField(verbose_name='Информация о персонале', max_length=500)
    country_from = models.CharField(verbose_name='Страна', max_length=150)
    slug = models.SlugField(max_length=100)
    
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Личный персонал'
        verbose_name_plural = 'Личный персонал'