from django.shortcuts import render
from django.http import HttpResponse

# Create our views here.
def index(request):
    return HttpResponse("Hello world - This is the pokemon listing")

