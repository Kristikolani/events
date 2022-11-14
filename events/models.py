from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class EventModel(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField((("picture")), upload_to='event/images/')
    date = models.DateField()


def __str__(self):
    return f"User {self.user}"

