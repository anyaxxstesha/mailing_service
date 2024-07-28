from django.forms import ModelForm

from clients.models import Client
from users.forms import StyleFormMixin


class ClientForm(StyleFormMixin, ModelForm):
    """
    Form for creating and updating clients.
    """
    class Meta:
        model = Client
        fields = ('email', 'name', 'surname', 'patronymic', 'comment')
