from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.RestaurantListView.as_view(), name='restaurant'),
]
