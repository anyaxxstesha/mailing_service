from django.forms import ModelForm

from mailings.models import Message
from users.forms import StyleFormMixin


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body', 'user')
