from django.conf.urls import url
from guests import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^login', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),
]
