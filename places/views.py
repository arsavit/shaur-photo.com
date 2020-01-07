from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Sity
# Create your views here.

class SityView(ListView):

    model = Sity
    queryset = Sity.objects.all()
    


class SityDetailView(DetailView):

    model = Sity
    slug_field = 'url'

