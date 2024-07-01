from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('list/', views.tweet_list, name='tweet_list'),
]
