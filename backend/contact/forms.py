from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Contact

class ContactForm(BSModalForm):
    class Meta:
        model = Contact
        fields = ('email', 'title', 'message')
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        return cleaned_data