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

        
class Rate(models.Model):
    efficiency = models.TextField(max_length = 50)
    care = models.TextField(max_length = 50)
    response = models.TextField(max_length = 50)
    average = models.TextField(max_length = 50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

class Services(models.Model):
    screenshot = models.ImageField(upload_to = 'images/')
    service_name = models.CharField(max_length =10)
    profile = models.ForeignKey(Profile, null = True,related_name='project')
    pub_date = models.DateTimeField(auto_now_add=True, null=True)
    user= models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
