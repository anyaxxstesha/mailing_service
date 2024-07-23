from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clients.forms import ClientForm
from clients.models import Client


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("clients:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("clients:client_detail", kwargs={"pk": self.object.pk})


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("clients:client_list")
