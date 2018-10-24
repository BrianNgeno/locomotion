from django.conf.urls import url
from . import views


urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
]