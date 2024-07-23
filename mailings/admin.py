from django.contrib import admin

from mailings.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'body', 'user')
    list_filter = ('user',)
    search_fields = ('subject',)
