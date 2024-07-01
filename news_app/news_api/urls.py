from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.keyword_create, name='keyword_create'),
    path('<int:keyword_id>/delete/', views.keyword_delete, name='keyword_delete'),
    path('list/', views.keyword_list, name='keyword_list'),
]
