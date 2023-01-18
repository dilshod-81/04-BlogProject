from django.shortcuts import render
from django.views.generic import ListView, DetailView
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