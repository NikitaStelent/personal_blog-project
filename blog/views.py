from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post, Category


def category_list_view(request):
    categories_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories_menu_list': categories_menu_list})


def category_view(request, ctg):
    # Получаем объект категории по ее имени
    category = Category.objects.filter(name__iexact=ctg).first()

    if category is None:
        raise Http404("Category not found")

    posts_categories = Post.objects.filter(category=category)
    return render(request, 'blog/categories.html', {'ctg': category, 'posts_categories': posts_categories})


class HomeView(ListView):
    model = Post
    template_name = 'blog/all_blogs.html'
    ordering = '-date'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/detailed_article.html'
    ordering = '-date'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'

    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(EditPostView, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:all_blogs')

    def get_context_data(self, *args, **kwargs):
        categories_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context['categories_menu'] = categories_menu
        return context
