from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
    path('register/', views.register, name='register'),
    # path('email/', views.email, name='email'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='forgot_password'),
    path('forgot_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='forgot_password_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='forgot_password_confirm'),
    path('forgot_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='forgot_password_complete'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservations/', views.reservations, name='reservations'),
    path('failed_reservation/', views.failed_reservation, name='failed_reservation'),
    path('failed_register/', views.failed_register, name='failed_register'),
    path('logout/', views.logout_view, name="logout"),
    path('clear_users', views.clear_users, name="clear_users")
]