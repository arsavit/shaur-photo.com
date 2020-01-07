from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views import generic
from django.views.generic.base import View

from .models import Price


# Create your views here.

class PriceView(ListView):
    model = Price
    queryset = Price.objects.all()

# class PriceDetDetailView(View):
#
#     def get(self, request):
#         price = Price.objects.all()
#         return render(request, 'price/price_detail.html', {'price': price})


class PriceDetailView(generic.DetailView):
    model = Price
    slug_field = 'url'

    def get_context_data(self, **kwargs):
        context = super(PriceDetailView, self).get_context_data(**kwargs)
        context['price_list'] = Price.objects.all()
        return context




