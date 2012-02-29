from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse
from store_locator.models import StoreLocator, DISTANCE_CHOICES, LocationType

class StoreLocatorPlugin(CMSPluginBase):
    """Subclass of Text plugin, includes 'topic' & 'css' fields"""

    model = StoreLocator
    name = _("Store Locator Map")
    render_template = "store_locator/store_locator_map.html"

    def render(self, context, instance, placeholder):
        get_lat_long_url = reverse('admin:get_lat_long_url')
        get_locations_url = reverse('admin:get_locations_url')
        location_types = LocationType.objects.all()
        context.update({
            'get_lat_long_url': get_lat_long_url,
            'get_locations_url': get_locations_url,
            'instance': instance,
            'distance_choices': DISTANCE_CHOICES,
            'location_types': location_types,
        })
        return context

plugin_pool.register_plugin(StoreLocatorPlugin)
