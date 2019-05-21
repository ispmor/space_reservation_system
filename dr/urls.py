from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('register/', views.register, name='register'),
    path('email/', views.email, name='email'),
]