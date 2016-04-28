from __future__ import unicode_literals
from django.http import request
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

from django.conf import settings
from guests.models import Guest
from rooms.models import Room


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    room = models.ForeignKey(Room)
    persons = models.PositiveIntegerField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()


    def __unicode__(self):
        return u"%s - booked - %s" % (self.user.first_name, self.room)

    def clean(self):
        checkin = self.checkin
        checkout = self.checkout
        room = self.room

        ''' Validates room capacity '''
        if self.room.category == 'Single' and self.persons > 1:
            raise ValidationError("Room can only accomdate 1 person")
        ''' Validates room capacity '''
        if self.room.category == 'Double' and self.persons > 2:
            raise ValidationError("Room can only accomdate 2 People")

        ''' This query will check if the date entered is booked already
            if yes it will assigne it to between.
            if between is assigned it will raise a ValidationError.
        '''
        between = Booking.objects.filter(
            Q(checkin__range=(checkin, checkout), room=room)
            | Q(checkout__range=(checkin, checkout), room=room)
            | Q(checkin__gte=checkin, checkout__lte=checkout, room=room)
        )
        if checkin and checkout:
            if between:
                raise ValidationError(
                    "Sorry, Room is already booked for this duration"
                )

        ''' This statment validates the checkout date is after the checking in
        date
        '''
        if checkout < checkin:
            raise ValidationError(
            "You can't Checkout before checkinging in"
            )
