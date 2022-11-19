import email
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


def register(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user1 = User.objects.get(username=request.POST["uname"])
                return render(
                    request, "register.html", {"error": "Username Has been Taken"}
                )
            except User.DoesNotExist:
                user1 = User.objects.create_user(
                    username=request.POST["number"],
                    first_name=request.POST["uname"],
                    email=request.POST["email"],
                    password=request.POST["password1"],
                )
                user1.save()
                auth.login(request, user1)
                return redirect("/")
        else:
            return render(
                request, "register.html", {"error": "Password Dose Not Match"}
            )
    else:
        return render(request, "register.html")


def delete(request, id):
    event_delete = EventModel.objects.get(id=id)
    print(event_delete)
    event_delete.delete()
    return redirect("/show")


@login_required
def profile(request):
    user = EventModel.objects.all()[0]
    return render(request, "profile.html", {"user": user})
