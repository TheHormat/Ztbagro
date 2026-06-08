from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from teserrufat.models import Service


class ServiceSiteMap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = 'https'

    def items(self):
        return Service.objects.all()

class Static_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 1
    protocol = 'https'

    def items(self):
        return ['home', 'about', 'contact', 'our_works']

    def location(self, item):
        return reverse(item)
