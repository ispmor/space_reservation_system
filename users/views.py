from django.shortcuts import render
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
# Create your views here.
from .forms import CustomUserCreationFormModal
from django.contrib.auth.forms import AuthenticationForm

class SignUpViewModal(BSModalCreateView):
    form_class = CustomUserCreationFormModal
    template_name = 'account/modals/signup.html'
    success_message = 'Success: Sign up succeeded. You can now Log in.'

class CustomLoginViewModal(BSModalLoginView):
    authentication_form = AuthenticationForm
    template_name = 'account/modals/login.html'
    success_message = 'Success: You were successfully logged in.'
