
from django.views.generic import ListView, DetailView

from .models import About, Desc
# Create your views here.

class AboutView(ListView):

    model = About
    queryset = About.objects.all()

class AboutDetailView(DetailView):

    model = About

