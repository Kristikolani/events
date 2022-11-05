import imp
from multiprocessing import context
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def registerPage(request):
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "register.html", context)