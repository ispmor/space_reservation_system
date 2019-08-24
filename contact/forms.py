from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import ContactRequest

class ContactForm(BSModalForm):
    class Meta:
        model = ContactRequest
        fields = ('email', 'title', 'message')
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        return cleaned_data