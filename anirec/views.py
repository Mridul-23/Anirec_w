from django.shortcuts import render, redirect
from .recommender import recommend, user_history, UCB
# Create your views here.
def start(request):
    if request.method == 'POST':
        return redirect('recommendation_process')

    return render(request, 'anirec/start.html')


def recommendation_process(request):
    # yet to make this view
    return render(request, 'anirec/recommender.html')