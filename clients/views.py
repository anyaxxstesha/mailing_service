from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client
from services.mixins import UsersQuerySetMixin, ObjectOwnerPermissionMixin


class ClientListView(LoginRequiredMixin, UsersQuerySetMixin, ListView):
    """
    List all clients.
    """
    model = Client
    view_permission = 'clients.view_client'


class ClientDetailView(LoginRequiredMixin, ObjectOwnerPermissionMixin,  DetailView):
    """
    Detail client.
    """
    model = Client
    permission_required = 'clients.view_client'


class ClientCreateView(LoginRequiredMixin, CreateView):
    """
    Create new client.
    """
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("clients:client_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ClientUpdateView(LoginRequiredMixin, ObjectOwnerPermissionMixin, UpdateView):
    """
    Update client.
    """
    model = Client
    form_class = ClientForm
    permission_required = 'clients.update_client'

    def get_success_url(self):
        return reverse("clients:client_detail", kwargs={"pk": self.object.pk})


class ClientDeleteView(LoginRequiredMixin, ObjectOwnerPermissionMixin, DeleteView):
    """
    Delete client.
    """
    model = Client
    success_url = reverse_lazy("clients:client_list")
    permission_required = 'clients.delete_client'
