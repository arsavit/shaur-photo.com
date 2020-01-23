from django.contrib.sitemaps import Sitemap
from .models import Album




class AlbumSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album.objects.all()

    def location(self, obj):
        return '/photosessions/svadebnaya_photosessiya/'

    def lastmod(self, obj):
        return obj.updated

