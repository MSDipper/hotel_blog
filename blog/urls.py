from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
    path('', views.PostListView.as_view(), name='blog'),
]
