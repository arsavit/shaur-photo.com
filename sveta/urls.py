"""sveta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from birthday_photosessiya.sitemaps import Album_birtSitemap, Album_birt_allSitemap
from aboutMe.sitemaps import AboutSitemap
from albums1.sitemaps import FotosetSitemap
from detskaya_photosessiya.sitemaps import Album_detSitemap, Album_det_allSitemap
from individualnaya_photosessiya.sitemaps import Album_ind_allSitemap, Album_indSitemap
from love_story_photosessiya.sitemaps import Album_love_allSitemap, Album_loveSitemap
from main.sitemaps import HeadersSitemap
from novogodnyaya_photosessiya.sitemaps import Album_nov_allSitemap, Album_novSitemap
from places.sitemaps import SitySitemap, Sity_allSitemap
from price.sitemaps import Price_allSitemap, PriceSitemap
from reviews.sitemaps import AutorSitemap
from semeynaya_photosessiya.sitemaps import Album_sem_allSitemap, Album_semSitemap
from svadebnaya_fotosessiya.sitemaps import Album_allSitemap, AlbumSitemap

sitemaps = {'queryset': Album_birtSitemap,
            'queryset2': AboutSitemap,
            'queryset3': Album_birt_allSitemap,
            'queryset4': FotosetSitemap,
            'queryset5': Album_detSitemap,
            'queryset6': Album_det_allSitemap,
            'queryset7': Album_indSitemap,
            'queryset8': Album_ind_allSitemap,
            'queryset9': Album_loveSitemap,
            'queryset10': Album_love_allSitemap,
            'queryset11': HeadersSitemap,
            'queryset12': Album_nov_allSitemap,
            'queryset13': Album_novSitemap,
            'queryset14': SitySitemap,
            'queryset15': Sity_allSitemap,
            'queryset16': PriceSitemap,
            'queryset17': Price_allSitemap,
            'queryset18': AutorSitemap,
            'queryset19': Album_sem_allSitemap,
            'queryset20': Album_semSitemap,
            'queryset21': Album_allSitemap,
            'queryset22': AlbumSitemap
            }



urlpatterns = [
    path('3773ex6/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('places/', include('places.urls')),
    path('aboutMe/', include('aboutMe.urls')),
    path('price/', include('price.urls')),
    path('photosessions/', include('albums1.urls')),
    path('photosessions/svadebnaya_photosessiya/', include('svadebnaya_fotosessiya.urls')),
    path('photosessions/individualnaya_photosessiya/', include('individualnaya_photosessiya.urls')),
    path('photosessions/semeynaya_photosessiya/', include('semeynaya_photosessiya.urls')),
    path('photosessions/detskaya_photosessiya/', include('detskaya_photosessiya.urls')),
    path('photosessions/birthday_photosessiya/', include('birthday_photosessiya.urls')),
    path('photosessions/novogodnyaya_photosessiya/', include('novogodnyaya_photosessiya.urls')),
    path('photosessions/love_story_photosessiya/', include('love_story_photosessiya.urls')),
    path('reviews/', include('reviews.urls')),
    path('', include('main.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
