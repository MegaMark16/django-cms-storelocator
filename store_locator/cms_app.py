"""Applications hooks for cmsplugin_zinnia"""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class StoreLocatorApphook(CMSApp):
    """Store Locator Apphook"""
    name = _('Store Locator')
    urls = ['store_locator.urls']

apphook_pool.register(StoreLocatorApphook)
