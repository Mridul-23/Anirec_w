from django.urls import path
from . import views

app_name = 'anirec'

urlpatterns = [
    path('start/', views.start, name='start'),
    path('search/', views.search_anime, name='search_anime'),
    path('recommender/', views.recommender_view, name='recommender'),
    path('recommendations/', views.get_recommendations, name='recommendations'),
]   