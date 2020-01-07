from django.urls import path

from . import views

urlpatterns = [
    path('', views.Album_birtListView.as_view(), name = 'birthday'),
    path('<slug:slug>/', views.Album_birtDetailView.as_view(),  name='album_birt_detail'),

]