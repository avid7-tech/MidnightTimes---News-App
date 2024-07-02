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
