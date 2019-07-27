from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('register/', views.register, name='register'),
    path('email/', views.email, name='email'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="password_change_form.html"), name='password_change'),
    path('password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="password_reset_form.html", email_template_name="password_reset_email.html"), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservations/', views.reservations, name='reservations'),
    path('concierge/', views.concierge, name='concierge'),
    path('failed_reservation/', views.failed_reservation, name='failed_reservation'),
    path('failed_register/', views.failed_register, name='failed_register'),
    path('logout/', views.logout_view, name="logout"),
    path('clear_users', views.clear_users, name="clear_users"),
    path('get_available_dates/', views.get_availale_time, name='get_abailable_time')
]