from django.shortcuts import render
from blog.models import *

from django.views.generic import ListView


class HomeListView(ListView):
    template_name = 'hotel/home.html'


class PostListView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/post_list.html'
    
    
# def blog_view(request):
#     post_list = Post.objects.all()
#     return render(request, 'blog/blog.html', {'post_list':post_list})