from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.Search.as_view(), name='search'),
    path('category/<slug:slug>/', views.GetCategoryListView.as_view(), name='get_category'),
    path('tag/<slug:slug>/', views.GetTagListView.as_view(), name='get_tag'),
    path('post_detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_single'),
    path('', views.PostListView.as_view(), name='post'),
]
