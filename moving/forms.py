from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Rate

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude =['user']