from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from  .models import Fotoset


class FotosetDetailView(ListView):
    model = Fotoset
    template_name = 'albums1/fotoset_detail.html'