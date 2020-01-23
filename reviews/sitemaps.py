from django.contrib.sitemaps import Sitemap
from .models import Autor




class AutorSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Autor.objects.all()

    def location(self, obj):
        return '/reviews/'

    def lastmod(self, obj):
        return obj.updated

