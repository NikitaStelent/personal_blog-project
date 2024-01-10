from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category


def category_view(request, ctg):
    # Получаем объект категории по ее имени
    category = Category.objects.filter(name__iexact=ctg).first()
    posts_categories = Post.objects.filter(category=category)
    return render(request, 'blog/categories.html', {'ctg': category, 'posts_categories': posts_categories})



class HomeView(ListView):
    model = Post
    template_name = 'blog/all_blogs.html'
    ordering = '-date'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/detailed_article.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'

    fields = '__all__'


class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ('title', 'body')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all_blogs')
