from django.shortcuts import render, redirect
from events.forms import EventForm
from events.models import EventModel
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView


def home(request):
    events = EventModel.objects.all()[:3]
    return render(request, 'home.html', {'events': events})


def about(request):
    return render(request, 'about.html')


def events(request):
    events = EventModel.objects.all()
    return render(request, 'events.html', {'events': events})


def add_event(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect("/")
    else:
        form = EventForm()
    return render(
        request,
        "event_form.html",
        {"form": form},
    )
