from django.shortcuts import render, redirect
from events.forms import EventForm
from events.models import EventModel
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


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


@login_required
def edit(request, id):
    if request.method == "POST":
        event = request.POST.get('event')
        # AUTH USER GET ID
        event_obj = EventModel.objects.get(id=id)
        event_obj.events = event
        event_obj.save()
        print("Event", event, "EVENTS", event_obj)
        return redirect('/events')
    else:
        # Return the particular value with id.
        event = EventModel.objects.filter(id=id)
        return render(request, 'edit_event.html', {'event': event})


def event_detail(request, pk):
    events = EventModel.objects.filter(id=pk)
    return render(request, "event_detail.html", {"events": events}) 
