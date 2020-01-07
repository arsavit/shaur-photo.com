from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Slider_down, Slider_head, Headers
from albums1.models import Fotoset

from love_story_photosessiya.models import Album_love
from semeynaya_photosessiya.models import Album_sem
from svadebnaya_fotosessiya.models import Album
from individualnaya_photosessiya.models import Album_ind
from birthday_photosessiya.models import Album_birt
from detskaya_photosessiya.models import Album_det
from novogodnyaya_photosessiya.models import Album_nov

# Create your views here.
class MainListView(ListView):
    model = Slider_head
    queryset = Slider_head.objects.all()
    def get_context_data(self, **kwargs):
        context = super(MainListView, self).get_context_data(**kwargs)
        context['slider_down_list'] = Slider_down.objects.all()
        context['fotoset_list'] = Fotoset.objects.all()
        context['album_sem_list'] = Album_sem.objects.all()
        context['album_ind_list'] = Album_ind.objects.all()
        context['album_list'] = Album.objects.all()
        context['album_birt_list'] = Album_birt.objects.all()
        context['album_nov_list'] = Album_nov.objects.all()
        context['album_love_list'] = Album_love.objects.all()
        context['album_det_list'] = Album_det.objects.all()
        context['headers'] = Headers.objects.all()
        return context