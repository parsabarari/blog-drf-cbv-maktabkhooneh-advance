from django.shortcuts import render
from django.views.generic import (
    ListView,
    FormView,
    CreateView,
    DetailView,
    CreateView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "parsa"
        return context


class PostCreateView(CreateView):
    model = Post
    fields = ["author", "title", "content", "status", "category", "published_date"]
    success_url = "/blog/post/"


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostUpdateView(UpdateView):
    model = Post
    fields = ["author", "title", "content", "status", "category", "published_date"]
    template_name_suffix = "_update_form"
    success_url = "/blog/post/"
