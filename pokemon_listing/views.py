from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests

# Create our views here.

# create a template (with import button)
# get this view to return the template
# create a URL that the button in template sends request to
# create method in this view to get the pokemon from the pokeAPI

def index(request):
    template = loader.get_template("listing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def fetchPokemon(request):
    template = loader.get_template("listing/import.html")
    data = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151&offset=0')
    context = {
        "pokemon": data.json()
    }
    return HttpResponse(template.render(context, request))
