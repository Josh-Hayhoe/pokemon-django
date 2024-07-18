from django.db import models

# Create your models here.
class Pokemon(models.Model):
    pokedex_entry = models.IntegerField(null=True)
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500, null=True)
    