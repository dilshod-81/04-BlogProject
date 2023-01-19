from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

class BlogListView(ListView):
    models = Post
    template_name = 'home.html'

    def get_queryset(self):
        """Return Schools """
        return Post.objects.order_by('id')

class BlogDetailView(DetailView):
    models = Post
    template_name = 'post_detail.html'

    def get_queryset(self):
        """Return Schools """
        return Post.objects.order_by('id')
class BlogCreateView(CreateView):
    models=Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

    def get_queryset(self):
        """Return Schools """
        return Post.objects.order_by('id')
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeletView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')