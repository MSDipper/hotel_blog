
from django.shortcuts import redirect, render
from django.views import View
from blog.models import *
from blog.forms import *
from django.views.generic import ListView, DetailView


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


class PostDetailView(DetailView):
    model = Post
    slug_url_kwarg = 'slug'
    template_name = 'blog/post_detail.html'


class AddComment(View):
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.post = post
            form.save()
        return redirect(post.get_absolute_url())