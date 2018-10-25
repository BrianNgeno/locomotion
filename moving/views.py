from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime as dt

# Create your views here.

def convert_dates(dates):
    # function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','thursday','Friday','Saturday','Sunday']
    '''
    Returns the actual day of the week
    '''
    day = days[day_number]
    return day


def home(request):
    return render(request,'main/home.html')

'''
logs out current user from account
'''
def logout(request):
    return render(request, 'main_pages/home.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('edit_profile')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit_profile.html', locals())

