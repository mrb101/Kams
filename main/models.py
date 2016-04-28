from __future__ import unicode_literals

from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Album(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    cover = models.BooleanField()
    image = models.ImageField(upload_to='gallery')
    image_thumb = ImageSpecField(source='image',
                                 processors=[ResizeToFill(100, 100)],
                                 format='JPEG',
                                 options={'quality': 60})
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
