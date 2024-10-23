from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls.base import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'web/base.html')


def register_view (request):

    if request.user.is_authenticated:
       return redirect(reverse('blog:index'))

    register_form = RegisterForm()

    if request.method == "POST":
     register_form = RegisterForm(request.POST)
     if register_form.is_valid():
        email = register_form.cleaned_data['email']
        username = register_form.cleaned_data['username']
        password = register_form.cleaned_data['password']
        User.objects.create_user(username=username,password=password,email=email)
        user = authenticate(request, username=username, password=password) 
        if user:
            login(request, user)
            return redirect(reverse('web:index'))


    return render (request, 'web/register.html', {'register_form': register_form})

def login_view (request):
    if request.user.is_authenticated:
       return redirect(reverse('blog:index'))

    login_form = LoginForm

    if request.method == 'POST':
        login_form =  LoginForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
               login(request, user)
               return redirect(reverse('blog:index'))


    return render (request, 'web/login.html',  {'login_form': login_form})

@login_required
def member_view(request):
   return render(request, 'web/member.html')

def logout_view (request):

   logout(request)
   return redirect(reverse('web:index'))




