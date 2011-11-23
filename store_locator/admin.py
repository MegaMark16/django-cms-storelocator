from django.contrib import admin, messages
from django.conf.urls.defaults import patterns, url
from models import Location
from django.conf import settings
from store_locator.views import get_lat_long

class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','phone', 'url')
    list_display_links = ('id','name',)
    list_filter = ('name',)
    
    fieldsets = (
        (None, {
            'fields': ('name',)
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
            url(r'^get_lat_long/$', get_lat_long)
        )
        return new_urls + old_urls

admin.site.register(Location, LocationAdmin)

