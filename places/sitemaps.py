from django.contrib.sitemaps import Sitemap
from .models import Places, Sity




class SitySitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Sity.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Sity_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Sity.objects.all()

    def location(self, obj):
        return '/places/'

    def lastmod(self, obj):
        return obj.updated
