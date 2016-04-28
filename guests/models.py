from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    ic = models.CharField(max_length=255, blank=False, null=False)
    band = models.ForeignKey('Band')

    def __unicode__(self):
        return self.user.first_name


class Address(models.Model):
    street = models.CharField(max_length=255, blank=False, null=False)
    state = models.CharField(max_length=255, blank=False, null=False)
    zip = models.CharField(max_length=255, blank=True, null=False)
    city = models.CharField(max_length=255, blank=False, null=False)
    country = models.CharField(max_length=255, blank=False, null=False)
    home_phone = models.CharField(max_length=255, blank=False, null=False)
    guest = models.ForeignKey(Guest)

    def __unicode__(self):
        return self.city


class Band(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=False)

    def __unicode__(self):
        return self.title
