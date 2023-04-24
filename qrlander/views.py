from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world!")

def index(request):
    return render(request, 'index.html')

class MyLoginView(LoginView):
    template_name = 'login.html'

def profile(request):
    return render(request, 'profile.html')

@login_required
def profile(request):
    return render(request, 'qrlander/profile.html')

class MyLoginView(LoginView):
    template_name = 'qrlander/login.html'

class MyLogoutView(LogoutView):
    next_page = 'login'