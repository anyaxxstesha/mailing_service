from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.forms import MessageForm, MailingForm
from mailings.models import Message, Mailing
from services.mixins import UsersQuerySetMixin


class MessageListView(LoginRequiredMixin, UsersQuerySetMixin, ListView):
    """
    List of all messages.
    """
    model = Message


class MessageDetailView(LoginRequiredMixin, UsersQuerySetMixin, DetailView):
    """
    Detail view of a message.
    """
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new message.
    """
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailings:message_list")


class MessageUpdateView(LoginRequiredMixin, UsersQuerySetMixin, UpdateView):
    """
    Update an existing message.
    """
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse("mailings:message_detail", kwargs={"pk": self.object.pk})


class MessageDeleteView(LoginRequiredMixin, UsersQuerySetMixin, DeleteView):
    """
    Delete an existing message.
    """
    model = Message
    success_url = reverse_lazy("mailings:message_list")


class MailingListView(LoginRequiredMixin, UsersQuerySetMixin, ListView):
    """
    List of all mailings.
    """
    model = Mailing


class MailingDetailView(LoginRequiredMixin, UsersQuerySetMixin, DetailView):
    """
    Detail view of a mailing.
    """
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new mailing.
    """
    model = Mailing
    form_class = MailingForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    success_url = reverse_lazy("mailings:mailing_list")


class MailingUpdateView(LoginRequiredMixin, UsersQuerySetMixin, UpdateView):
    """
    Update an existing mailing.
    """
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse("mailings:mailing_detail", kwargs={"pk": self.object.pk})


class MailingDeleteView(LoginRequiredMixin, UsersQuerySetMixin, DeleteView):
    """
    Delete an existing mailing.
    """
    model = Mailing
    success_url = reverse_lazy("mailings:mailing_list")
