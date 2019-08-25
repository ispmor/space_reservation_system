from django.urls import path

from .views import CustomLoginViewModal, SignUpViewModal

urlpatterns = [
    path('login/', CustomLoginViewModal.as_view(), name='login'),
    path('signup/', SignUpViewModal.as_view(), name='signup'),
]
