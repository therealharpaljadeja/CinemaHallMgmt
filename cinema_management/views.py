from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .models import Screens
from .models import Movies
from .models import Staff
from .models import FoodStall
from django.http import Http404
from django.template import loader

