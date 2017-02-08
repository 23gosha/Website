from django.contrib import admin

# Register your models here.

from .models import Album
from .models import Song

admin.site.register(Album) # Album calss should have an admin interface
admin.site.register(Song)