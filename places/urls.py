from django.urls import path

from . import views


urlpatterns = [
    path('', views.SityView.as_view(), name = 'places'),
    path('<slug:slug>/', views.SityDetailView.as_view(), name='sity_detail')
]