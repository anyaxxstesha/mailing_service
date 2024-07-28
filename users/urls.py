from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserResetView, UserBanView, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password-reset/', UserResetView.as_view(template_name='users/reset_form.html'), name='reset'),
    path('', UserListView.as_view(), name='user_list'),
    path('ban/<int:pk>/', UserBanView.as_view(), name='ban'),
]
