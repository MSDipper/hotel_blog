from django.shortcuts import render
from django.views import View
from restaurant.models import *
from django.views.generic import ListView

def home(request):
    return render(request, 'home/home_list.html')



# class HomeListView(ListView):
#     template_name = 'home/home_list.html'


# class CategoryMenuForHomeListView(ListView):
    
    # def get_queryset(self):
    #     return RangeMenu.objects.filter(category_menu__slug=self.kwargs.get('slug'))
    
