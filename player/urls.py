from django.urls import path

from . import views


app_name = "player"


urlpatterns = [
    path('', views.index, name='index'),
    path('add_channel/', views.add_channel, name='add_channel'),
    path('play_channel/', views.play_channel, name='play_channel'),
    path('stop_music/', views.stop_music, name='stop_music'),
]
