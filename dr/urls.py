from django.urls import path, include
from django.contrib import admin

from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('email/', views.email, name='email'),
    path(settings.PASSWORD_CHANGE_URL, auth_views.PasswordChangeView.as_view(template_name="password_change_form.html"), name='password_change'),
    path(settings.PASSWORD_CHANGE_URL + '/done', auth_views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name='password_change_done'),
    path(settings.PASSWORD_RESET_URL, auth_views.PasswordResetView.as_view(template_name="password_reset_form.html", email_template_name="password_reset_email.html"), name='password_reset'),
    path(settings.PASSWORD_RESET_URL + '/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path(settings.PASSWORD_RESET_URL + '/complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
    path(settings.RESERVATION_URL, views.reservation, name='reservation'),
    path(settings.RESERVATIONS_URL, views.reservations, name='reservations'),
    path(settings.CONCIERGE_URL, views.concierge, name='concierge'),
    path(settings.FAILED_RESERVATION_URL, views.failed_reservation, name='failed_reservation'),
    path(settings.FAILED_REGISTER_URL, views.failed_register, name='failed_register'),
    path(settings.LOGOUT_URL, views.logout_view, name="logout"),
    path('clear_users', views.clear_users, name="clear_users"),
    path('get_available_dates/', views.get_availale_time, name='get_available_time'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('create/', views.ReservationCreateView.as_view(), name='create_reservation'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('update/<uidb64>', views.ReservationUpdateView.as_view(), name='update_reservation'),
    path('read/<uidb64>', views.ReservationReadView.as_view(), name='read_reservation'),
    path('delete/<uidb64>', views.ReservationDeleteView.as_view(), name='delete_reservation'),
]