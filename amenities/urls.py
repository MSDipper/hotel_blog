from django.urls import path
from . import views

urlpatterns = [
    path('', views.AmenitiesListView.as_view(), name='services')
]
