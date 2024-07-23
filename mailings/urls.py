from django.urls import path


from mailings.apps import MailingsConfig
from mailings.views import MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('mailings/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('mailings/create/', MessageCreateView.as_view(), name='message_create'),
    path('mailings/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('mailings/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
]
