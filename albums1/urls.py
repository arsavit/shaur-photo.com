from django.urls import path

from . import views




urlpatterns = [
    path('', views.FotosetDetailView.as_view(), name = 'photosessions')
]