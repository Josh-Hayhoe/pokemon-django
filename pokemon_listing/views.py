from django.http import HttpResponse
from django.template import loader
from pokemon_listing.models import Pokemon
import requests

# Create our views here.

def index(request):
    template = loader.get_template("listing/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def fetchPokemon(request):
    template = loader.get_template("listing/import.html")
    # get the data from pokeAPI
    response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=151&offset=0')
    data = response.json()

    list = []
    # Iterate over the JSON and create models
    for index, pokemon in enumerate(data['results']):
        res = requests.get(pokemon['url'])
        itemMeta = res.json()
        # Create the model and save i to the database
        # TODO - check if the entry already exists in the DB and skip if it does
        item = Pokemon(
            number=index+1,
            name=pokemon['name'],
            url=pokemon['url'],
            sprite_url=itemMeta['sprites']['back_default']
        )
        item.save()
        # TODO - load the data from the database - currently the pokeAPI is hit every page load,
        # TODO - we want to load from the DB once the data is imported
        # Add the current pokemon to the list to return to the frontend
        # for now until we add querying the database
        list.append(item)

    context = {
        "pokemon": list,
    }
    return HttpResponse(template.render(context, request))


