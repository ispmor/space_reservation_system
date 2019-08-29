from datetime import datetime
from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from bootstrap_modal_forms.forms import BSModalForm
from .models import Reservation

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
    