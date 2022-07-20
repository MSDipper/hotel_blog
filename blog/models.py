from email import message
from unicodedata import category
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

from django.urls import reverse


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
    description = RichTextField(blank=True, null=True)
    slug = models.SlugField(max_length=150)
    category = models.ForeignKey(Category, related_name='post', verbose_name='Категория', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='post', verbose_name='Теги')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_single", kwargs={'slug':self.slug})
    
    def get_comment(self):
        return self.comment.filter(parent__isnull=True)
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

class Popular(models.Model):
    add_popular = models.ManyToManyField(Post, verbose_name='Попурярное')
    slug = models.SlugField(max_length=150)
    
    
    def __str__(self):
        return f'{self.add_popular}'
    
    
    class Meta:
        verbose_name = 'Попурярное'
        verbose_name_plural = 'Попурярное'


class Comment(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=150)
    email = models.EmailField(max_length=254)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    image = models.ImageField(verbose_name='Изображения', upload_to='image/', blank=True, null='True')
    message = models.TextField(max_length=500, verbose_name='Текст')
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length=150, blank=True, null='True')
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'



