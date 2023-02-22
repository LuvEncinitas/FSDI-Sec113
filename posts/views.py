from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    DetailView,
    ListView,
)
from .models import Post
from django.urls import reverse_lazy


class PostView(ListView):
    template_name = "post/list.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "post/detail.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "post/new.html"
    model = Post
    fields =["title", "subtitle", "author", "body", "active"]

class PostUpdateView(UpdateView):
    template_name = "post/edit.html"
    model = Post
    fields =["title", "subtitle", "author", "active"]

class PostDeleteView(DeleteView):
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("list")


