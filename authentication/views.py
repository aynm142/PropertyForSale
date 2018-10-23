from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.views.generic import CreateView
from django.contrib.auth import login, authenticate
from .models import Profile


# Create your views here.
def signup(request):
    user_form = UserForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username, password)
    else:
        return render(request, 'auth/create.html', {'user_form': user_form, 'profile_form': profile_form})
