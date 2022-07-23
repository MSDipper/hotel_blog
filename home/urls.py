from django.urls import path
from . import views
from home.views import home

urlpatterns = [
    path('', home, name='home'),
    # path('', views.HomeListView.as_view(), name='home')
]
