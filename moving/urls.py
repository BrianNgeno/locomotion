from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^edit$', views.edit, name='edit_profile'),
    url(r'^rate/',views.rate_site, name='rate'),
    url(r'^booking(?P<service_id>\d+)',views.book, name='booking'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^add(?P<service_id>\d+)',views.add, name='add'),
    url(r'^drop/(?P<service_id>\d+)',views.drop, name='drop'),
    url(r'^one_service(?P<service_id>\d+)',views.service, name='service'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
