from django.views.generic import ListView, DetailView

from .models import Album_love
from semeynaya_photosessiya.models import Album_sem
from svadebnaya_fotosessiya.models import Album
from individualnaya_photosessiya.models import Album_ind
from birthday_photosessiya.models import Album_birt
from detskaya_photosessiya.models import Album_det
from novogodnyaya_photosessiya.models import Album_nov

# Create your views here.

class Album_loveListView(ListView):
    model = Album_love
    queryset = Album_love.objects.all()
    template_name = 'love_story_photosessiya/album_list.html'
    paginate_by = 9


class Album_loveDetailView(DetailView):
    model = Album_love
    slug_field = 'url'
    template_name = 'love_story_photosessiya/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(Album_loveDetailView, self).get_context_data(**kwargs)
        context['album_sem_list'] = Album_sem.objects.all()
        context['album_ind_list'] = Album_ind.objects.all()
        context['album_list'] = Album.objects.all()
        context['album_birt_list'] = Album_birt.objects.all()
        context['album_nov_list'] = Album_nov.objects.all()
        context['album_love_list'] = Album_love.objects.all()
        context['album_det_list'] = Album_det.objects.all()
        return context
