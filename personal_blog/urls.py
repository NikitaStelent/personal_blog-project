from django.contrib import admin
from django.urls import path, include

from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', include('blog.urls')),
    path('users/', include('users.urls')),
]
