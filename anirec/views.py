import json
from .recommender import UCB
from django.http import JsonResponse
from anime.models import GeneralData
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.contrib.auth.decorators import login_required
from .session_helpers import initialize_user_history, update_user_history

def start(request):
    if request.method == 'POST':
        return redirect('recommendation_process')

    return render(request, 'anirec/start.html')

@require_GET
def search_anime(request):
    name = request.GET.get('name')
    payload = []
    
    if name:
        names_english_objs = GeneralData.objects.filter(name_english__icontains=name)
        for obj in names_english_objs:
            payload.append(obj.name_english)

    return JsonResponse({'status': 200, 'data': payload})

@login_required(login_url='user:login')
def recommender_view(request):
    if request.method == 'GET':
        return render(request, 'anirec/recommender.html')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        initialize_user_history(request.session, data)

        return JsonResponse({'status': 'success', 'message': 'Data processed successfully'})
    
@login_required(login_url='user:login')
def get_recommendations(request):

    if request.method == 'GET':
        recommendations = UCB(request.session)
        context = {
            'data' : []
        }

        for anime in recommendations:
            context['data'].append(GeneralData.objects.filter(unique_id=anime).first())

        
        return render(request, 'anirec/recommendations.html', context=context)
    else :
        show1_rating = int(request.POST.get('show1_rating'))
        show2_rating = int(request.POST.get('show2_rating'))
        show3_rating = int(request.POST.get('show3_rating'))

        if not (1 <= show1_rating <= 5) or not (1 <= show2_rating <= 5) or not (1 <= show3_rating <= 5):
            return JsonResponse({'status': 'failed', 'message': 'Ratings must be between 1 and 5.'}, status=400)

        update_user_history(request.session, show1_rating, show2_rating, show3_rating)
        
        recommendations = UCB(request.session)
        context = {
            'data' : []
        }

        for anime in recommendations:
            context['data'].append(GeneralData.objects.filter(unique_id=anime).first())

        return render(request, 'anirec/recommendations.html', context=context)