from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('', include('blog.urls', namespace='blog')),
    path('clients/', include('clients.urls', namespace='clients')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
