from django.db import models

class Name(models.Model):
    pokedex_entry = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=500, null=True)
    def __str__(self):
        return self.name

# Create your models here.
