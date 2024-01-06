from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'category', 'title', 'body')

    widgets = {
        'author': forms.Select(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category', 'title', 'body')

    widgets = {
        'category': forms.Select(attrs={'class': 'form-control'}),
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }
