from django.forms import ModelForm

from mailings.models import Message, Mailing
from users.forms import StyleFormMixin


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = ('subject', 'body', 'user')


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('name', 'message', 'clients', 'started_at', 'completed_at', 'frequency')


class MailingBanForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('is_banned',)
