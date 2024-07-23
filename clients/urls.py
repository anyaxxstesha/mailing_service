from django.urls import path

from blog.apps import BlogConfig
from clients.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]
