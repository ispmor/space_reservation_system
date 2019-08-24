from django.urls import path

from .views import CustomLoginViewModal, SignUpViewModal

urlpatterns = [
    path('login-modal/', CustomLoginViewModal.as_view(), name='login-modal'),
    path('signup/', SignUpViewModal.as_view(), name='signup'),

]
