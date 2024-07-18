from rest_framework import serializers
from .models import Pokemon

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields=("pokedex_entry", "name", "url")