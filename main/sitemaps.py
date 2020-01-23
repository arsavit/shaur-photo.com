from django.contrib.sitemaps import Sitemap
from .models import Headers




class HeadersSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Headers.objects.all()

    def location(self, obj):
        return ''

    def lastmod(self, obj):
        return obj.updated

