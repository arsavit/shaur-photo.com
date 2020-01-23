from django.contrib.sitemaps import Sitemap
from .models import Album_love


def lastmod(obj):

    return obj.updated


class Album_loveSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album_love.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_love_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album_love.objects.all()

    def location(self, obj):
        return '/photosessions/love_story_photosessiya/'

    def lastmod(self, obj):
        return obj.updated
