from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ProfileForm,RateForm,NewsLetterForm,CommentForm,PaymentForm,BookingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime as dt
from .models import NewsLetterRecipients,Profile,Rate,Services,Payment, Booking
from .email import send_welcome_email
from django.http import JsonResponse

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
    rateform = RateForm()
    form = NewsLetterForm()
    date = dt.date.today()
    service = Services.objects.all()
    print(service)
    return render(request,'main/home.html', locals())

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

@login_required(login_url='/accounts/login')
def rate_site(request):
    profile = User.objects.get(username=request.user)
    if request.method == 'POST':
        rateform = RateForm(request.POST, request.FILES)
        print(rateform.errors)
        if rateform.is_valid():
            rating = rateform.save(commit=False)
            rating.user = request.user
            rating.save()
            return redirect('home')
    else:
        rateform = RateForm()
    return render(request,'main/home.html',locals())

def newsletter(request):
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()
    send_welcome_email(name, email)
    data = {'success': 'You have been successfully added to mailing list'}
    return JsonResponse(data)

def view_project(request):
    service = Services.objects.all()
    return render(request,'home.html', locals())

@login_required(login_url='/accounts/login')
def add(request,service_id):
    service = Services.objects.get(id=service_id)
    current_user = request.user
    current_user.profile.service = service
    current_user.profile.save()
    return redirect('service',service_id)

@login_required(login_url='/accounts/login')
def drop(request,service_id):
    current_user = request.user
    current_user.profile.service = None
    current_user.profile.save()
    return redirect('home')

@login_required(login_url='/accounts/login/')
def service(request,service_id):
    current_user = request.user
    name = current_user.profile.service
    single_service = Services.objects.get(id = request.user.profile.service.id)
    # comments = Comment.objects.all()
    # form = CommentForm(instance=request.user)

    return render(request,'main/service.html',locals())

@login_required(login_url='/accounts/login/')
def edit(request):
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

@login_required(login_url='/accounts/login/')
def book(request,service_id):
    profile = User.objects.get(username=request.user)
    service = Services.objects.get(id=service_id)
    single_service = Services.objects.get(id = request.user.profile.service.id)
    if request.method == 'POST':
        bookingform = BookingForm(request.POST, request.FILES)
        if bookingform.is_valid():
            edit = bookingform.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('home')
    else:
        bookingform = BookingForm()
    return render(request, 'main/payment.html', locals())


@login_required(login_url='/accounts/login/')
def bookingform(request,service_id):
    service = Services.objects.get(id=service_id)
    bookingform = BookingForm()
    # bookingform = ProfileForm()
    single_service = Services.objects.get(id = request.user.profile.service.id)
    return render(request,'main/payment.html',  {'bookingform':bookingform, 'single_service':single_service})