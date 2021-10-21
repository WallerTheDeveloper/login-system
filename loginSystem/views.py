from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import Profile
from django.contrib.auth import login, authenticate, logout

def mainPage(request):
    return render(request, 'main.html')

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('mainPage')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
            else: print("Username OR password is incorrect")
    else: form = UserCreationForm()

    return render(request, 'pages/login-register-page.html', {'page': page, 'form': form})

def logoutUser(request):
    logout(request)
    return render(request, 'pages/login-register-page.html')

def registerUser(request):
    page = 'register'
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'page': page, 'form': form}
    return render(request, 'pages/login-register-page.html', context)