from django.shortcuts import render
from blog.models import *

from django.views.generic import ListView


class HomeListView(ListView):
    template_name = 'hotel/home.html'


def blog_view(request):
    post_list = Post.objects.all()
    return render(request, 'blog/blog.html', {'post_list':post_list})