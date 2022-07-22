from atexit import register
from django import template

from about.models import *

register = template.Library()



@register.simple_tag()
def get_customer():
    return Customer.objects.all()



@register.simple_tag()
def get_customerperson():
    return CustomerPerson.objects.all()