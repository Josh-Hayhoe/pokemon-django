from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def index(request):
    return HttpResponse(f"Hello world - This is the pokemon listing")