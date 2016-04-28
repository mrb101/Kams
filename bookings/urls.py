from django.conf.urls import url
from bookings import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$', views.bookings, name='bookings'),
    url(r'^(?P<pk>\d+)/$', views.booking, name='booking'),
    url(r'^(?P<pk>\d+)/delete', views.delete_booking, name='delete_booking')
]
