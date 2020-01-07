from django.urls import path

from . import views

urlpatterns = [
    path('', views.Album_loveListView.as_view(), name = 'love_story'),
    path('<slug:slug>/', views.Album_loveDetailView.as_view(),  name='album_love_detail'),

]