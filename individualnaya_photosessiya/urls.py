from django.urls import path

from . import views

urlpatterns = [
    path('', views.Album_indListView.as_view(), name = 'individualnaya'),
    path('<slug:slug>/', views.Album_indDetailView.as_view(),  name='album_ind_detail'),

]