from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Album, Foto
from semeynaya_photosessiya.models import Album_sem
from individualnaya_photosessiya.models import Album_ind
from birthday_photosessiya.models import Album_birt
from detskaya_photosessiya.models import Album_det
from love_story_photosessiya.models import Album_love
from novogodnyaya_photosessiya.models import Album_nov
# Create your views here.

class AlbumListView(ListView):
    model = Album
    queryset = Album.objects.all()
    template_name = 'svadebnaya_fotosessiya/album_list.html'


class AlbumDetailView(DetailView):
    model = Album
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['album_sem_list'] = Album_sem.objects.all()
        context['album_ind_list'] = Album_ind.objects.all()
        context['album_list'] = Album.objects.all()
        context['album_birt_list'] = Album_birt.objects.all()
        context['album_nov_list'] = Album_nov.objects.all()
        context['album_love_list'] = Album_love.objects.all()
        context['album_det_list'] = Album_det.objects.all()
        return context