from django.db import models

# Create your models here.

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    sprite_url = models.CharField(max_length=255)
