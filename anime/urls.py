from django.urls import path
from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.home, name='home'),
    path('anime_details/<int:unique_id>', views.anime_details, name='anime_details'),
    path('search/', views.search_anime, name='search_anime')
]