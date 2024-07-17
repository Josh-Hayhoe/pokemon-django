from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from pokemon_listing.models import Name
from django.core import serializers
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
    num =0
    poke_list = ""
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
    response_data = r.json()
    for item in response_data["results"]:
        name = response_data["results"][num]["name"] + "\n"
        poke_list += name
        num+=1
    return HttpResponse(poke_list)

