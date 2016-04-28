from __future__ import unicode_literals

from django.db import models


class Room(models.Model):
    SINGLE = 'Single'
    DOUBLE = 'Double'
    category_choices = (
        (SINGLE, 'Single'),
        (DOUBLE, 'Double')
    )
    number = models.CharField(max_length=5)
    category = models.CharField(max_length=10,
                                choices=category_choices,
                                default=SINGLE)
    active = models.BooleanField(default=True)
    smoking = models.BooleanField(default=False)

    def __unicode__(self):
        return "{0} | {1}".format(self.number, self.category)


class Facility(models.Model):
    room = models.ManyToManyField(Room)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __unicode__(self):
        return self.name
