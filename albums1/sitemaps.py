from django.contrib.sitemaps import Sitemap
from .models import Fotoset




class FotosetSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Fotoset.objects.all()

    def location(self, obj):
        return '/photosessions/'

    def lastmod(self, obj):
        return obj.updated

