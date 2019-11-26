from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.all_games, name='index'),
    url(r'^Welcome/', views.Welcome),
    url(r'^register/', views.viewRegister, name='viewRegister'),
    url(r'^index/', views.all_games, name='all_games'),
]