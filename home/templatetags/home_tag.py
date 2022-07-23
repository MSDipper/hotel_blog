from atexit import register
from django import template
from rooms.models import *
from blog.models import Post
from about.models import About, Customer, CustomerPerson
from restaurant.models import *
from django.db.models import Count


register = template.Library()



@register.simple_tag
def get_room_post():
    return Room.objects.all()

@register.simple_tag
def get_about_post():
    return About.objects.all()

@register.simple_tag
def get_blog_post(count=3):
    return Post.objects.order_by('id')[:count]



@register.simple_tag
def get_rangemenu_post(count=3):
    return RangeMenu.objects.order_by('id')[:count]



@register.simple_tag()
def get_customer():
    return Customer.objects.all()



@register.simple_tag()
def get_customerperson():
    return CustomerPerson.objects.all()



@register.simple_tag()
def get_categories_menu_for_home():
    ''' Вывод всех категорий меню '''
    return CategoryMenu.objects.all()