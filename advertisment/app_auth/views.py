from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from  .forms import RegisterFrom
from .models import Profile

def login_view(request):
    redirect_url = reverse('main_page')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
        
    username = request.POST['userame']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/login.html')

def profile_view(request):
    return render(request, 'app_auth/profile.html')

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if request.method == 'POST':
        form = RegisterFrom(request.POST) 
        if form.is_valid(): 
            form.save()

            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            
            user = authenticate(username=username, password=password)
            login(request, user)

            url = reverse('main_page')
            return redirect(url) 
    else: 
        form = RegisterFrom() 
    context = {'form':form} 
    return render(request, 'app_auth/register.html', context) 
