from django.urls import path

from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from blog.apps import BlogConfig


app_name = BlogConfig.name

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('blog/create/', PostCreateView.as_view(), name='post_create'),
    path('blog/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('blog/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
