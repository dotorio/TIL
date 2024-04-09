from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:profile', form.get_user().username)
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)
    
def profile(request, username):
    profile_owner = User.objects.get(username=username)
    context = {
        'profile_owner' : profile_owner
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, profile_owner_pk):
    profile_owner = User.objects.get(pk=profile_owner_pk)
    if request.user in profile_owner.follower.all():
        profile_owner.follower.remove(request.user)
    else:
        profile_owner.follower.add(request.user)
    return redirect('accounts:profile', profile_owner.username)

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')