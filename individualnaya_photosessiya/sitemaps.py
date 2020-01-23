from django.contrib.sitemaps import Sitemap
from .models import Album_ind


def lastmod(obj):

    return obj.updated


class Album_indSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album_ind.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_ind_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album_ind.objects.all()

    def location(self, obj):
        return '/photosessions/individualnaya_photosessiya/'

    def lastmod(self, obj):
        return obj.updated

