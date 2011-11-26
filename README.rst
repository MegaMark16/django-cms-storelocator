django-cms-storelocator
=================
An extension for Django CMS that lets you enter your store locations and 
drop a plugin on any page that generates a map and store list based on 
city/state or zip code search input, or a city drop down for each city
with a location in it.

Dependancies
============

- django (tested with 1.3)
- django-cms (tested with 2.2)

Getting Started
=============

To get started simply install using ``pip``:
::
    pip install django-cms-storelocator

Add ``store_locator`` to your installed apps and ``syncdb`` (or migrate, if 
you have south installed).

Your installed apps should look something like this:
::
	INSTALLED_APPS = (
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.sites',
	    'django.contrib.messages',
	    'django.contrib.admin',
	    'cms',
	    'store_locator',
	)

Finally, add store_locator.urls to your urls.py so that we can make a few 
ajax calls needed to interact with the map.  Here's what a simple urls.py
might look like:
::
    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^store-locator/', include('store_locator.urls')),
        url(r'^', include('cms.urls')),
    )
	
Usage
=============

You can add store locations through the admin, the app will try to find a 
lat/long via google maps api if you do not enter them.

Once you have your locations entered you can simply drop a Store Locator 
plugin on any page in your Django CMS implementation and it will render
a google map, a search field, a search distance drop down, and a search 
button.  When a user searchs for an address, zip code, city, or any other 
location information that Google Maps can translate into an address, the
plugin will show markers on the map for any Store Locations that are 
within the distance specified by the user of the address they searched for.

