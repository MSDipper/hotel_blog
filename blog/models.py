from email import message
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



class Tag(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    slug = models.SlugField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=150)
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ImageField(upload_to='image/', verbose_name='Фото')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=150)
    comments = models.ForeignKey("Comment", verbose_name='Коментарии', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.ManyToManyField(Tag, verbose_name='Теги')

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Popular(models.Model):
    add_popular = models.ManyToManyField(Post, verbose_name='Попурярное')
    slug = models.SlugField(max_length=150)
    
    
    def __str__(self):
        return self.add_popular
    
    
    class Meta:
        verbose_name = 'Попурярное'
        verbose_name_plural = 'Попурярное'


class Comment(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=500, verbose_name='Текст')
    slug = models.SlugField(max_length=150)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

class Paragraph(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст')
    
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текст'


