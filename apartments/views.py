from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm
from django.views.generic.edit import CreateView
from django.contrib.auth import login, authenticate
from .models import Profile


# Create your views here.
# def user_create(request):
#     user_form = UserForm()
#     profile_form = ProfileForm()
#     return render(request, 'auth/create.html', {'user_form': user_form, 'profile_form': profile_form})


class SignUpView(CreateView):
    model = Profile
    fields = ['phone_number']
    form_class = ProfileForm
    template_name = 'auth/create.html'

    # def form_valid(self, form):
    #     form.save()
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password1')
    #     user = authenticate(username=username, password=password)
    #     login(self.request, user)
    #     return redirect('/admin')
