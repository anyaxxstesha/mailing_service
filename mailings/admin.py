from django.contrib import admin

from mailings.models import Message, Mailing


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'user')
    list_filter = ('user',)
    search_fields = ('subject',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status', 'completed_at', 'started_at', 'frequency', 'message')
    list_filter = ('status',)
    search_fields = ('name',)
