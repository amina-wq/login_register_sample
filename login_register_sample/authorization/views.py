from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'login.html', {})
    elif request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is None:
            return render(request, 'login.html', {})
        else:
            login(request, user)
            return redirect(reverse('home'))
    else:
        raise Exception('Method is not allowed')


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect(reverse('login'))


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'register.html', {})
    elif request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create(
            username=email,
            password=make_password(password),
            first_name=name,
            last_name=surname,
            email=email
        )
        return redirect(reverse('login'))
    else:
        raise Exception('Method is not allowed')


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')