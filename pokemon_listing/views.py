from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests
from pokemon_listing.models import Name
from django.core import serializers
from api.views import getData
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
    url = ""
    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151&offset=0")
    response_data = r.json()
    for item in response_data["results"]:
        #get the name of pokemon
        poke_name = response_data["results"][num]["name"]
        #concatenate to string
        poke_list += poke_name + "\n"
        #get url for more info
        url = response_data["results"][num]["url"]
        num+=1
        #save pokemon to database
        name = Name(pokedex_entry = num, name = poke_name, url = url)
        name.save()
    # "print" onto web page
    return HttpResponse(poke_list)



 