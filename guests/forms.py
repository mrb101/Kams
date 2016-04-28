from django import forms
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from models import Guest


class GuestRegisterationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username',
                  'password')


class GuestProfileForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['dob', 'ic']
