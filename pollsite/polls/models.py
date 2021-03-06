from django.db import models
from django.forms import CharField, EmailField

# Create your models here.
class User(models.Model):
    name = CharField(max_length=200)
    email = EmailField(blank=True)
    password = CharField(max_length=100)
    invite_code = 2