from django.contrib import admin, messages
from models import Location
from django.conf import settings

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','phone', 'url')
    list_display_links = ('id','name',)
    list_filter = ('name',)

admin.site.register(Location, LocationAdmin)

