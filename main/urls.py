from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^album/$', views.album, name='album'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^services/$', views.services, name='services'),
]
