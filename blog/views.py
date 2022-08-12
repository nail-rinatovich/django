# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView # новое
from django.urls import reverse_lazy # импортируем новые методы
from django.shortcuts import render
from django import forms
from .models import Post, Category

class BlogListView(ListView):
    model = Post
    template_name = 'category-list.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'content']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content']


class BlogDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('category-list.html')
class CategoryListView(ListView):
    model = Category
    template_name = "category_list.html"


class PostByCategoryView(ListView):
    context_object_name = 'posts'
    template_name = 'post_list.html'

    def get_queryset(self):
        self.category = Category.objects.get(slug=self.kwargs['slug'])
        queryset = Post.objects.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category
        return context
