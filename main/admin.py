from django.contrib import admin

from imagekit.admin import AdminThumbnail
from models import Gallery, Album


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'admin_thumbnail')
    admin_thumbnail = AdminThumbnail(image_field='image_thumb')

admin.site.register(Album)
admin.site.register(Gallery, GalleryAdmin)
