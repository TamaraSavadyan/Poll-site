from django.shortcuts import render
from django.views.generic import CreateView
from .models import User

# Create your views here.
class UserView(CreateView):
    model = User
    fields = ('name', 'email', 'password', 'verification_code')

    