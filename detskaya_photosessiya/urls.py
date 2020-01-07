from django.urls import path

from . import views

urlpatterns = [
    path('', views.Album_detListView.as_view(), name = 'detskaya'),
    path('<slug:slug>/', views.Album_detDetailView.as_view(),  name='album_det_detail'),

]