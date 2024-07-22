from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('title',)
