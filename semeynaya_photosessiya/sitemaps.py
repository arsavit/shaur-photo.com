from django.contrib.sitemaps import Sitemap
from .models import Album_sem




class Album_semSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):

        return Album_sem.objects.all()

    def lastmod(self, obj):
        return obj.updated

class Album_sem_allSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.9

    def items(self):
        return Album_sem.objects.all()

    def location(self, obj):
        return '/photosessions/semeynaya_photosessiya/'

    def lastmod(self, obj):
        return obj.updated
