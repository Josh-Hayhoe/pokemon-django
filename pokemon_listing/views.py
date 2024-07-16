from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create our views here.

# create a template (with import button)
# get this view to return the template
# create a URL that the button in template sends request to
# create method in this view to get the pokemon from the pokeAPI

def index(request):
    return HttpResponse(f"Hello world - This is the pokemon listing")