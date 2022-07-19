from atexit import register
from django import template

from blog.models import *
from django.db.models import Count

register = template.Library()

# @register.simple_tag()
# def get_categories():
#     ''' Вывод всех категориев '''
#     return Category.objects.annotate(category_count=Count('post')).all()


@register.simple_tag()
def get_tags():
    ''' Вывод всех тегов '''
    return Tag.objects.all()

# @register.inclusion_tag('blog/include/tags/popular_articles.html')
# def get_popular_articles_post():
#     return Category.objects.all()


@register.inclusion_tag('blog/include/tags/popular_articles.html')
def get_popular_articles_post(count=4):
    post_list = Post.objects.order_by('id')[:count]
    return {'post_list':post_list}


@register.inclusion_tag('blog/include/tags/tag.html')
def get_tags():
    tags_list = Tag.objects.all()
    return {'tags_list':tags_list}


@register.inclusion_tag('blog/include/tags/category_tag.html')
def get_categories():
    categories = Category.objects.annotate(category_count=Count('post')).all()
    return {'categories':categories}


@register.inclusion_tag('blog/include/tags/search_tag.html')
def get_search():
    pass