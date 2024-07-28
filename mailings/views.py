from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from mailings.forms import MessageForm, MailingForm, MailingBanForm
from mailings.models import Message, Mailing
from services.mixins import UsersQuerySetMixin, ObjectOwnerPermissionMixin, UpdateObjectOwnerPermissionMixin


class MessageListView(LoginRequiredMixin, UsersQuerySetMixin, ListView):
    """
    List of all messages.
    """
    view_permission = 'mailings.view_message'
    model = Message


class MessageDetailView(LoginRequiredMixin, ObjectOwnerPermissionMixin, DetailView):
    """
    Detail view of a message.
    """
    model = Message
    permission_required = 'mailings.view_message'


class MessageCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new message.
    """
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailings:message_list")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class MessageUpdateView(LoginRequiredMixin, ObjectOwnerPermissionMixin, UpdateView):
    """
    Update an existing message.
    """
    model = Message
    form_class = MessageForm
    permission_required = 'mailings.change_message'

    def get_success_url(self):
        return reverse("mailings:message_detail", kwargs={"pk": self.object.pk})


class MessageDeleteView(LoginRequiredMixin, ObjectOwnerPermissionMixin, DeleteView):
    """
    Delete an existing message.
    """
    model = Message
    success_url = reverse_lazy("mailings:message_list")
    permission_required = 'mailings.delete_message'


class MailingListView(LoginRequiredMixin, UsersQuerySetMixin, ListView):
    """
    List of all mailings.
    """
    model = Mailing
    view_permission = 'mailing.view_mailing'


class MailingDetailView(LoginRequiredMixin, ObjectOwnerPermissionMixin, DetailView):
    """
    Detail view of a mailing.
    """
    model = Mailing
    permission_required = 'mailing.view_mailing'


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


class MailingUpdateView(LoginRequiredMixin, UpdateObjectOwnerPermissionMixin, UpdateView):
    """
    Update an existing mailing.
    """
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailings.can_ban_mailing'
    permission_form_class = MailingBanForm

    def get_success_url(self):
        return reverse("mailings:mailing_detail", kwargs={"pk": self.object.pk})


class MailingDeleteView(LoginRequiredMixin, ObjectOwnerPermissionMixin, DeleteView):
    """
    Delete an existing mailing.
    """
    model = Mailing
    success_url = reverse_lazy("mailings:mailing_list")
    permission_required = 'mailing.delete_mailing'
