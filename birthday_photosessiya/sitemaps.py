from django.contrib.sitemaps import Sitemap
from .models import Album_birt






class Album_birtSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album_birt.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_birt_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album_birt.objects.all()

    def location(self, obj):
        return '/photosessions/birthday_photosessiya/'

    def lastmod(self, obj):
        return obj.updated
