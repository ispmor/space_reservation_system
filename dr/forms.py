from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Reservation
from .models import ContactRequest
from datetime import datetime
from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm

class CustomUserCreationForm(PopRequestMixin, CreateUpdateAjaxMixin,
                             UserCreationForm):

    group = forms.MultipleChoiceField(choices = (('s', 'Student'),('l', 'Lecturer'),('x', 'External')))
    class Meta:
        model = User
        exclude = ['last_login', 'superuser_status', 'user_permissions', 'active', 'staff', 'date_joined']
        fields = ['username', 'email', 'first_name','last_name', 'group']

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        return cleaned_data

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        room = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}))
        fields = ['room', 'start_reservation', 'end_reservation', 'description']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_reservation'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_reservation'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
    def clean(self):
        
        cleaned_data = super(ReservationForm, self).clean()
        if cleaned_data['start_reservation'] > cleaned_data['end_reservation']:
            raise forms.ValidationError("Provided dates are incorrect. Please provide dates in proper order.")

        return cleaned_data
    
class ContactForm(BSModalForm):
    class Meta:
        model = ContactRequest
        fields = ('email', 'title', 'message')
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        return cleaned_data

class ModalReservationForm(BSModalForm):
    class Meta:
        model = Reservation
        # exclude = ['statu']
        fields = ['room']



class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']