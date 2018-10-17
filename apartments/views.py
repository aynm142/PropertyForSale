from django.shortcuts import render
from .forms import UserForm, ProfileForm


# Create your views here.
def user_create(request):
    print(1)
    user_form = UserForm()
    profile_form = ProfileForm()
    return render(request, 'auth/create.html', {'user_form': user_form, 'profile_form': profile_form})
