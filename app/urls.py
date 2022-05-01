from django.urls import path, include
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed/', views.video_feed, name='video_feed'),
     path('mask_feed', views.mask_feed, name='mask_feed'),
]