from django.urls import path

from . import views

urlpatterns = [
    path('', views.Album_semListView.as_view(), name = 'semeynaya'),
    path('<slug:slug>/', views.Album_semDetailView.as_view(),  name='album_sem_detail'),

]