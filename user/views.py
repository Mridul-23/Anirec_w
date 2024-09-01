from .forms import CustomUserCreationForm, CustomLoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib import messages
from anime.models import GeneralData, Saved_anime
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            messages.success(request, 'Signup successful!')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/signup.html', {'form': form})


def login(request):
    form = CustomLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('user:user_home')
    return render(request, 'user/login.html', {'form': form})

@login_required(login_url='login')
def user_home(request):
    saved_anime = Saved_anime.objects.filter(user=request.user)
    return render(request, 'user/user_home.html', {'saved_anime': saved_anime})


def logout(request):
    auth_logout(request)
    return redirect('anime:home')