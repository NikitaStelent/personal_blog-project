from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, EditPostView, DeletePostView, category_view, \
    category_list_view

app_name = 'blog'

urlpatterns = [
    path('blog/', HomeView.as_view(), name='all_blogs'),
    path('blog/article/<int:pk>', ArticleDetailView.as_view(), name='detailed_article'),
    path('blog/add_post/', AddPostView.as_view(), name='add_post'),
    path('blog/article/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('blog/article/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('blog/category/<str:ctg>/', category_view, name='category'),
    path('blog/category_list/', category_list_view, name='category_list'),
]

