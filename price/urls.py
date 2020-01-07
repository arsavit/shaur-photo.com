from django.urls import path

from . import views

urlpatterns = [
    path('', views.PriceView.as_view(), name = 'price'),
    path('<slug:slug>/', views.PriceDetailView.as_view(),  name='price_detail'),

]
