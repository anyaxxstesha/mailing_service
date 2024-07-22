from django.contrib import admin

from clients.models import Client


@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'surname')
    list_filter = ('id',)
    search_fields = ('email',)
