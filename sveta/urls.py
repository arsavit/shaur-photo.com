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

urlpatterns = [
    path('top_secret/', admin.site.urls),
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
    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
