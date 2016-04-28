from django.conf.urls import url
from rooms import views

urlpatterns = [
    url(r'^rooms/$', views.index, name='rooms'),
    url(r'^rooms/(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^rooms/(>P<id>\d+)/facilties/$',
        views.facilties, name='room_facilities'
        ),
]
