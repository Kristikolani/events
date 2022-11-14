import email
from turtle import title
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render, get_list_or_404
from django.http import HttpResponse
from events.models import EventModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .forms import *


def login(request):
    if request.method == "POST":
        email1 = request.POST.get('email')
        password = request.POST.get('password')
        print(email1, password)
        user_auth = auth.authenticate(username=email1, password=password)
        print("USER_AUTH", user_auth)
        if user_auth is not None:
            auth.login(request, user_auth)
            print(user_auth)
            messages.success(request, 'Auth User')
            return redirect('/')
        else:
            messages.success(request, 'User not found')
        return redirect('/')
    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                user1 = User.objects.get(username=request.POST['uname'])
                return render(request, 'register.html', {'error': "Username Has been Taken"})
            except User.DoesNotExist:
                user1 = User.objects.create_user(username=request.POST['number'], first_name=request.POST['uname'], email=request.POST['email'], password=request.POST['password1'])
                user1.save()
                auth.login(request, user1)
                return redirect('/')
        else:
            return render(request, 'register.html', {'error': "Password Dose Not Match"})
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def delete(request, id):
    event_delete = EventModel.objects.get(id=id)
    print(event_delete)
    event_delete.delete()
    return redirect('/show')


@login_required
def profile(request):
    user = EventModel.objects.all()[0]
    return render(request, "profile.html", {"user": user})

