from django.shortcuts import render
from bootstrap_modal_forms.generic import (BSModalLoginView,
                                           BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from django.urls import reverse_lazy, resolve, reverse

from .forms import ContactForm                                    
class ContactView(BSModalCreateView):
    form_class = ContactForm
    template_name = 'contact/modals/contact.html'
    success_message = 'Success: You successfully contacted us!.'
    success_url = reverse_lazy('home')
