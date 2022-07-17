from atexit import register
from django import template

from blog.models import *
from django.db.models import Count

register = template.Library()

@register.simple_tag()
def get_categories():
    ''' Вывод всех категориев в блог '''
    return Category.objects.annotate(category_count=Count('categories')).all()