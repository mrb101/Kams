from django import forms
from django.db.models import Q
from rooms.models import Room
from models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'persons', 'checkin', 'checkout']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'persons': forms.NumberInput(attrs={'class': 'form-control'}),
            'checkin': forms.DateInput(attrs={'class': 'form-control',
                                              'id': 'datepicker',
                                              'placeholder': 'yyyy-mm-dd'}),
            'checkout': forms.DateInput(attrs={'class': 'form-control',
                                               'id': 'datepicker',
                                               'placeholder': 'yyyy-mm-dd'})
        }
