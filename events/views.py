from django.shortcuts import render, redirect
from .models import Event
from django.http import HttpRequest, HttpResponse


def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


def about(request):
    return render(request, 'about.html')


def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})


def add_event(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = Event(request.POST)
        
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect("event-detail", pk=events.pk)
    else:
        form = Event()
    return render(
        request,
        "event_form.html",
        context={"form": form},
    )
