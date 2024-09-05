from django.urls import path
from . import views

app_name = 'anirec'

urlpatterns = [
    path('start/', views.start, name='start'),
    path('recommender/', views.recommendation_process, name='recommender')
]   