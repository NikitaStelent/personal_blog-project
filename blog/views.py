from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post


# Create your views here.
# def home(request):
#     return render(request, 'blog/all_blogs.html', {})

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


