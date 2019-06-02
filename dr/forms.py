from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from datetime import datetime

class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    group = forms.MultipleChoiceField(choices = (('s', 'Student'),('l', 'Lecturer'),('x', 'External')))
    class Meta:
        model = User
        exclude = ['last_login', 'superuser_status', 'user_permissions', 'active', 'staff', 'date_joined']
        fields = ['username', 'email','password', 'confirm_password', 'first_name','last_name', 'group']

    def clean(self):
        cleaned_data = super(UserCreateForm, self).clean()
        if cleaned_data['password'] != cleaned_data['confirm_password']:
            raise forms.ValidationError("Provided passwords are incorrect. Please correct them.")
        return cleaned_data

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        #exclude = ['user', 'id', 'indeks', 'status']
        room = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}))
        fields = ['room', 'start_reservation', 'end_reservation']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['room'].widget.attrs.update({'class': 'form-control'})
        self.fields['start_reservation'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_reservation'].widget.attrs.update({'class': 'form-control'})
    def clean(self):
        
        cleaned_data = super(ReservationForm, self).clean()
        
        if cleaned_data['start_reservation'] > cleaned_data['end_reservation']:
            raise forms.ValidationError("Provided dates are incorrect. Please provide dates in proper order.")

        return cleaned_data
    

  