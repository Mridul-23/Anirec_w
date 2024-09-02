from django.urls import path
from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_anime, name='search_anime'),
    path('anime_details/<int:unique_id>', views.anime_details, name='anime_details'),
    path('save_anime/<int:anime_id>/', views.save_anime, name='save_anime')
]   