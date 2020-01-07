from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Album_sem
from svadebnaya_fotosessiya.models import Album
from individualnaya_photosessiya.models import Album_ind
from birthday_photosessiya.models import Album_birt
from detskaya_photosessiya.models import Album_det
from love_story_photosessiya.models import Album_love
from novogodnyaya_photosessiya.models import Album_nov

# Create your views here.

class Album_semListView(ListView):
    model = Album_sem
    queryset = Album_sem.objects.all()
    template_name = 'semeynaya_photosessiya/album_list.html'


class Album_semDetailView(DetailView):
    model = Album_sem
    slug_field = 'url'
    template_name = 'semeynaya_photosessiya/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Album_semDetailView, self).get_context_data(**kwargs)
        context['album_sem_list'] = Album_sem.objects.all()
        context['album_ind_list'] = Album_ind.objects.all()
        context['album_list'] = Album.objects.all()
        context['album_birt_list'] = Album_birt.objects.all()
        context['album_nov_list'] = Album_nov.objects.all()
        context['album_love_list'] = Album_love.objects.all()
        context['album_det_list'] = Album_det.objects.all()
        return context