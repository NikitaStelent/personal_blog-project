from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/registration/register.html'
    success_url = reverse_lazy('users:login')


class UserLoginView(LoginView):
    template_name = 'users/registration/login.html'
    success_url = reverse_lazy('blog:all_blogs')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


def profile(request):
    user = request.user
    return render(request, 'users/profile.html', {'user': user})
