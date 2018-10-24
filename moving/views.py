from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'main/home.html')

'''
logs out current user from account
'''
def logout(request):
    return render(request, 'main_pages/home.html')
