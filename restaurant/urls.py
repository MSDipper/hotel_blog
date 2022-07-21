from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.GetCategoryMenuListView.as_view(), name='get_category_menu'),
    path('', views.RestaurantListView.as_view(), name='restaurant'),
]
