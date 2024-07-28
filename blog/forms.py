from django.forms import ModelForm

from blog.models import Post
from users.forms import StyleFormMixin


class PostForm(StyleFormMixin, ModelForm):
    """
    Form for creating and updating blog posts.
    """
    class Meta:
        model = Post
        fields = ('title', 'content', 'preview_image')
