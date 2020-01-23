from django.contrib.sitemaps import Sitemap
from .models import Album_nov



class Album_novSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album_nov.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_nov_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album_nov.objects.all()

    def location(self, obj):
        return '/photosessions/novogodnyaya_photosessiya/'

    def lastmod(self, obj):
        return obj.updated
