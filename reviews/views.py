from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Autor, Body, Foto


class ReviewsListView(ListView):
    model = Autor
    queryset = Autor.objects.all()
    template_name = 'reviews/reviews_list.html'

class ReviewsDetailView(DetailView):

    model = Autor
