from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.keyword_create, name='keyword_create'),
    path('<int:keyword_id>/delete/', views.keyword_delete, name='keyword_delete'),
    path('list/', views.keyword_list, name='keyword_list'),
    path('control/', views.control, name='control'),
    # 
    path('control/block/<int:user_id>/', views.block_user, name='block_user'),
    path('control/set_limit/<int:user_id>/', views.set_limit, name='set_limit'),
    
    path('login/', views.signin, name='signin'),
    path('not_authorized/', views.not_authorized, name='not_authorized'),
    
    path('search-history/', views.search_history, name='search_history'),
]
"""
URL configuration for the Django application.

This `urlpatterns` list routes URLs to views. For example:
- The home page view is accessible at the root URL ('').
- The user registration view is accessible at 'register/'.
- The keyword creation view is accessible at 'create/'.
- The keyword deletion view is accessible at '<int:keyword_id>/delete/'.
- The keyword list view is accessible at 'list/'.
- The control panel view is accessible at 'control/'.
- The block user view is accessible at 'control/block/<int:user_id>/'.
- The set user limit view is accessible at 'control/set_limit/<int:user_id>/'.
- The sign-in view is accessible at 'login/'.
- The not authorized view is accessible at 'not_authorized/'.
- The search history view is accessible at 'search-history/'.

Each path is associated with a specific view function in the views module.
"""