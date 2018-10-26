from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


        
class Profile(models.Model):
    Profile_photo = models.ImageField(upload_to = 'images/',blank=True)
    Bio = models.TextField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    service = models.ForeignKey('Services', related_name='services',null=True)

    def save_profile(self):
        self.save()

    @classmethod
    def get_by_id(cls, id):
        details = Profile.objects.get(user = id)
        return details

    @classmethod
    def filter_by_id(cls, id):
        details = Profile.objects.filter(user = id).first()
        return details
    
    @classmethod
    def search_user(cls, name):
        userprof = Profile.objects.filter(user__username__icontains = name)
        return userprof

        
class Rate(models.Model):
    efficiency = models.TextField(max_length = 50,null=True)
    care = models.TextField(max_length = 50,null=True)
    response = models.TextField(max_length = 50,null=True)
    average = models.TextField(max_length = 50,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    
  
    def __str__(self):
        return self.design

    # class Meta:
    #     ordering = ['id']

    def save_rate(self):
        self.save()

    @classmethod
    def get_rate(cls, profile):
        rate = Rate.objects.filter(Profile__pk = profile)
        return rate
    
    @classmethod
    def get_all_rating(cls):
        rating = Rate.objects.all()
        return rating

class Payment(models.Model):
    pay = models.CharField(max_length=30)
    user = models.ForeignKey(User,related_name='user',null=True)

    def save_service(self):
        self.save()
    
    @classmethod
    def get_payment(cls, service):
        pay = Payment.objects.filter(service__pk = service)
        return pay

class Booking(models.Model):
    location = models.CharField(max_length = 50,null=True)
    number = models.CharField(max_length = 50,null=True)
    email = models.CharField(max_length = 50,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    payment = models.ForeignKey(Payment,related_name='booking',null=True)

    def save_service(self):
        self.save()

class Services(models.Model):
    screenshot = models.ImageField(upload_to = 'images/',null=True)
    service_name = models.CharField(max_length =50,null=True)
    profile = models.ForeignKey(Profile, null = True,related_name='project')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length =60,null=True)
    payment = models.ForeignKey('Payment',related_name='payment',null=True)

    class Meta:
        ordering = ['-pk']

    def save_service(self):
        self.save()
    
    @classmethod
    def get_service(cls, profile):
        project = Services.objects.filter(Profile__pk = profile)
        return project
    
    @classmethod
    def get_all_services(cls):
        project = Services.objects.all()
        return project

  
    @classmethod
    def find_service_id(cls, id):
        identity = Services.objects.get(pk=id)
        return identity

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Comment(models.Model):
    name = models.CharField(max_length=30)
    service = models.ForeignKey(Services,related_name='comment')
    user = models.ForeignKey(User,null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    @classmethod
    def find_commentpost(cls,id):
        comments = Comments.objects.filter(post__pk = id)
        return comments

    