from django.forms import fields
from events.models import EventModel
from django import forms
from django.contrib.auth import models  


class EventForm(forms.Form):
    class Meta:
        title = forms.CharField(max_length=100)


class UpdateForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['title']
        widgets = {
            'events': forms.TextInput(attrs={'class': 'form__field'})
        }
