from atexit import register
from django import template

from restaurant.models import *

register = template.Library()



@register.simple_tag()
def get_categories_menu():
    ''' Вывод всех категорий меню '''
    return CategoryMenu.objects.all()