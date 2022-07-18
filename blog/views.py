from typing import List
from django.shortcuts import render
from blog.models import *

from django.views.generic import ListView


class HomeListView(ListView):
    template_name = 'hotel/home.html'


class PostListView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/post_list.html'
    
    # def get_queryset(self):
    #     return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')

    
# def blog_view(request):
#     post_list = Post.objects.all()
#     return render(request, 'blog/blog.html', {'post_list':post_list})

class GetCategoryListView(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class GetTagListView(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


class Search(ListView):
    paginate_by = 6
    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("q"))
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context
        