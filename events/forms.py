from pyexpat import model

from events.models import EventModel
from django import forms


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = [
            "title",
            "description",
            'date',
            "image",
        ]
