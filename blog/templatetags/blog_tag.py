from atexit import register
from django import template

from blog.models import *
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def get_categories():
    ''' Вывод всех категориев '''
    return Category.objects.annotate(category_count=Count('post')).all()


@register.simple_tag()
def get_tags():
    ''' Вывод всех тегов '''
    return Tag.objects.all()