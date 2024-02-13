
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mainapp.formulario import RegisterForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'mainapp/index.html', {'title':'inicio'})