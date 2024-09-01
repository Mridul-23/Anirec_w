from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import GeneralData, AdminChoices
from .contentfilter import recommend
# Create your views here.

from django.shortcuts import render
from .models import GeneralData, Genre, AdminChoices

def home(request):
    if request.method == 'GET':
        # Admin's recommendations
        admins_recommendations = AdminChoices.objects.all()
        anime_data = [GeneralData.objects.get(unique_id=i.index) for i in admins_recommendations]

        # Get Genre objects for Action, Adventure, and Romance
        action_genre = Genre.objects.get(name="Action")
        adventure_genre = Genre.objects.get(name="Adventure")
        romance_genre = Genre.objects.get(name="Romance")

        # Filter anime data by genre
        action_anime_data = GeneralData.objects.filter(genre=action_genre).order_by('?')[0:10]
        adventure_anime_data = GeneralData.objects.filter(genre=adventure_genre).order_by('?')[0:10]
        romance_anime_data = GeneralData.objects.filter(genre=romance_genre).order_by('?')[0:10]

        # Context for the template
        context = {
            'anime_data': anime_data,
            'action_anime_data': action_anime_data,
            'adventure_anime_data': adventure_anime_data,
            'romance_anime_data': romance_anime_data,
        }
    else:
        context = {}

    return render(request, 'anime/home.html', context=context)

def anime_details(request, unique_id):
    anime = get_object_or_404(GeneralData, unique_id=unique_id)
    recommendations = recommend(anime.name_english, top=12)
    similar_animes = GeneralData.objects.filter(name_english__in=recommendations)
    context = {
        'anime': anime,
        'similar_animes': similar_animes,
    }
    return render(request, 'anime/anime_details.html', context=context)


def search_anime(request):
    query = request.GET.get('search', '')
    anime_filter = request.GET.get('filter', 'popularity')
    print(f"Search Query: {query}")
    anime_list = GeneralData.objects.all()

    if anime_filter == 'favorites':
        anime_filter = f'-{anime_filter}'

    if query:
        anime_list = anime_list.filter(
            Q(name__icontains=query) | Q(name_english__icontains=query)
        ).order_by(anime_filter)
    else:
        anime_list = anime_list.order_by(anime_filter)

    print(f"Number of results: {anime_list.count()}")
    
    paginator = Paginator(anime_list, per_page=24)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'anime_list': page_obj,
        'page_obj': page_obj,
        'query': query,
        'anime_filter': anime_filter
    }


    return render(request, 'anime/search.html', context=context)