from django.contrib.sitemaps import Sitemap
from .models import About




class AboutSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return About.objects.all()

    def location(self, obj):
        return '/aboutMe/'

    def lastmod(self, obj):
        return obj.updated


