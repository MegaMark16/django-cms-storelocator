from django.contrib import admin, messages
from django.conf.urls.defaults import patterns, url
from models import Location, LocationType
from django.conf import settings
from store_locator.views import get_lat_long, get_locations

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','phone', 'url')
    list_display_links = ('id','name',)
    list_filter = ('name',)
    
    fieldsets = (
        (None, {
            'fields': ('name','location_types',)
        }),
        ('Address', {
            'fields': ('address', ('latitude', 'longitude'))
        }),
        ('Other Information', {
            'fields': ('phone', 'url', 'description')
        }),
    )
    class Media:
        js = ("store_locator/js/store_locator_admin.js",)
        
    def get_urls(self):
        old_urls = super(LocationAdmin, self).get_urls()
        new_urls = patterns('',
            url(r'^get_lat_long/$', get_lat_long, name='get_lat_long_url'),
            url(r'^get_locations/$', get_locations, name='get_locations_url'),
        )
        return new_urls + old_urls

admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType)

