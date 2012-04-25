import urllib2
import urllib 
import json

from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from store_locator.models import StoreLocator, DISTANCE_CHOICES, LocationType, Location

def show_locations(request):
    get_lat_long_url = reverse('get_lat_long_url')
    get_locations_url = reverse('get_locations_url')
    location_types = LocationType.objects.all()
    params = {
        'get_lat_long_url': get_lat_long_url,
        'get_locations_url': get_locations_url,
        'distance_choices': DISTANCE_CHOICES,
        'location_types': location_types,
    }
    return render_to_response('store_locator/store_locator_map_view.html', params, context_instance=RequestContext(request))

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
        distance = int(request.GET.get('distance', 0))
        location_type = request.GET.get('location_type', '0')
    except:
        return HttpResponse('[]')
    
    locations = Location.objects.near(latitude, longitude, distance)
    if location_type:
        locations = [l for l in locations if location_type in [str(t[0]) for t in l.location_types.values_list('id')]]
    json_locations = []
    locations.sort(key=lambda loc: loc.distance)
    for location in locations:
        location_dict = {}
        location_dict['id'] = location.id
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
