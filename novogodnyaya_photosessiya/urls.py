from django.urls import path

from . import views

urlpatterns = [
    path('', views.Album_novListView.as_view(), name = 'novogodnyaya'),
    path('<slug:slug>/', views.Album_novDetailView.as_view(),  name='album_nov_detail'),

]