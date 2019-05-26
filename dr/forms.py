from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Reservation
from datetime import datetime

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    group = forms.ChoiceField(required=True, choices=[('student', 'lecturer', 'extern')])
    first_name = forms.CharField(required=True)
    second_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ("first_name", "second_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.group = self.cleaned_data["group"]
        user.second_name = self.cleaned_data["second_name"]
        user.firs_name = self.cleaned_data["first_name"]
        if commit:
            user.save()
        return user

# class UserCreateForm(forms.Form):
#     first_name = forms.CharField(
#         required = True,
#         label = 'first_name',
#         max_length = 32
#     )
#     second_name = forms.CharField(
#         required = True,
#         label = 'second_name',
#         max_length = 32
#     )
#     email = forms.EmailField(
#         required = True,
#         label = 'Email'
#     )
#     password = forms.CharField(
#         required = True,
#         label = 'Password',
#         max_length = 32,
#         widget = forms.PasswordInput()
#     )
#     group = forms.ChoiceField(
#         required=True, 
#         choices=[('student', 'lecturer', 'extern')]
#     )

class ReservationForm(forms.ModelForm):
    start_reservation = forms.DateTimeField()
    class Meta:
        model = Reservation
        exclude = ['user', 'id', 'indeks', 'status']

    def clean(self):
        
        cleaned_data = super(ReservationForm, self).clean()
        
        if cleaned_data['start_reservation'] > cleaned_data['end_reservation']:
            raise forms.ValidationError("Provided dates are incorrect. Please provide dates in proper order.")

        return cleaned_data
    

  