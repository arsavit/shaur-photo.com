from django.contrib.sitemaps import Sitemap
from .models import Album_det


def lastmod(obj):

    return obj.updated


class Album_detSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album_det.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_det_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album_det.objects.all()

    def location(self, obj):
        return '/photosessions/detskaya_photosessiya/'

    def lastmod(self, obj):
        return obj.updated

