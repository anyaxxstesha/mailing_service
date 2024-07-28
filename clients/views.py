from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client
from services.mixins import UsersQuerySetMixin


class ClientListView(LoginRequiredMixin, UsersQuerySetMixin, ListView):
    """
    List all clients.
    """
    model = Client


class ClientDetailView(LoginRequiredMixin, UsersQuerySetMixin, DetailView):
    """
    Detail client.
    """
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Create new client.
    """
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("clients:client_list")


class ClientUpdateView(LoginRequiredMixin, UsersQuerySetMixin, UpdateView):
    """
    Update client.
    """
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("clients:client_detail", kwargs={"pk": self.object.pk})


class ClientDeleteView(LoginRequiredMixin, UsersQuerySetMixin, DeleteView):
    """
    Delete client.
    """
    model = Client
    success_url = reverse_lazy("clients:client_list")
