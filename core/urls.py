
from django.urls import path
from .views import create_post, PostListView,PostDetailView

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
] 