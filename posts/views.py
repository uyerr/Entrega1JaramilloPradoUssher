from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

#  title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    success_url = '/posts/'
    template_name = 'post_create.html'
    fields = ['title', 'slug', 'author', 'content', 'status']
    
    
class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    success_url = '/posts/'
    template_name = 'post_edit.html'
    fields = ['title', 'slug', 'author', 'content', 'status']
    
    
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/posts/'
    template_name = 'post_delete.html'


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

