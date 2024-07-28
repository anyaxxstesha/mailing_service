from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post
from services.utils import get_posts_from_cache


class PostListView(ListView):
    """
    Displays a list of 3 blog posts.
    """
    model = Post

    def get_queryset(self):
        return get_posts_from_cache()


class PostDetailView(DetailView):
    """
    Detail view for one post
    """
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_amount += 1
        self.object.save()
        return self.object


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Create a new post
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:post_list")
    permission_required = 'blog.add_post'


class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Update an existing post
    """
    form_class = PostForm
    model = Post
    permission_required = 'blog.change_post'

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Delete a post
    """
    model = Post
    success_url = reverse_lazy("blog:post_list")
    permission_required = 'blog.delete_post'
