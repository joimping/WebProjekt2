from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ContactForm (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=250)
    email = models.EmailField(max_length=250, default=" ")
    created_at = models.DateTimeField(default=timezone.now)

