from django.contrib.sitemaps import Sitemap
from .models import Price




class PriceSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Price.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Price_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Price.objects.all()

    def location(self, obj):
        return '/price/'

    def lastmod(self, obj):
        return obj.updated


