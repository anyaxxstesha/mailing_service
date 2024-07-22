from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):

        return self.model.objects.filter(is_published=True).order_by("?")[:3]


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_amount += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    fields = ("title", "content", "preview_image")
    success_url = reverse_lazy("blog:post_list")


class PostUpdateView(UpdateView):
    model = Post
    fields = ("title", "content", "preview_image")

    def get_success_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:post_list")
