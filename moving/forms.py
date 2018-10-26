from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Rate,Services,Payment,Comment,Booking

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','service']

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude =['user']
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        exclude = ['user','profile']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
 
class CommentForm(forms.Form):
    class Meta:
        model = Comment
        exclude = ['user','service']

class PaymentForm(forms.Form):
    class Meta:
        model = Payment
        exclude = ['user']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ['user','payment']