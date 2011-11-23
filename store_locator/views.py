import urllib2
import urllib 
import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from store_locator.models import Location

def get_lat_long(request):
    if not request.GET.get('q'):
        return HttpResponse('')
    args = urllib.urlencode({'q': request.GET.get('q')})
    r = urllib2.urlopen("http://maps.google.com/maps/geo?output=csv&%s" % args)
    return HttpResponse(r.read())

def get_locations(request):
    try:
        latitude = float(request.GET.get('lat'))
        longitude = float(request.GET.get('long'))
        distance = int(request.GET.get('distance', 25))
    except:
        return HttpResponse('[]')

    locations = Location.objects.near(latitude, longitude, distance)
    json_locations = []
    for location in locations:
        location_dict = {}
        location_dict['name'] = location.name
        location_dict['address'] = location.address
        location_dict['latitude'] = location.latitude
        location_dict['longitude'] = location.longitude
        location_dict['distance'] = location.distance
        location_dict['description'] = location.description
        location_dict['url'] = location.url
        location_dict['phone'] = location.phone
        json_locations.append(location_dict)
    return HttpResponse(json.dumps(json_locations), mimetype="application/json")
