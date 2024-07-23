from django.forms import ModelForm

from clients.models import Client
from users.forms import StyleFormMixin


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('email', 'name', 'surname', 'patronymic', 'comment')
