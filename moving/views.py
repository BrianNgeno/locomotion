from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

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