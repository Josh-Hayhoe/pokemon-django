from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from pokemon_listing.models import Name
# Create our views here.

# create a template (with import button)
# get this view to return the template
# create a URL that the button in template sends request to
# create method in this view to get the pokemon from the pokeAPI


def button(request):
    template = loader.get_template("listing/button.html")
    context = {}
    return HttpResponse(template.render(context, request))

def fetch_pokemon(request):
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
#for item in r:
        #name = Name(name=item[0])
        #name.save()
        #Able to save to the db in the shell but not here, plus it didnt show up in the physical db anyway
    return HttpResponse(r)