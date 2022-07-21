from django.shortcuts import render
from django.views.generic import ListView
from restaurant.models import *


class RestaurantListView(ListView):
    model = RangeMenu
    template_name = 'restaurant/rangemenu_list.html'
    

class GetCategoryMenuListView(ListView):

    def get_queryset(self):
        return RangeMenu.objects.filter(category_menu__slug=self.kwargs.get('slug')).select_related('category_menu')
        


