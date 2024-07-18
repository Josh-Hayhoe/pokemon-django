from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data
from pokemon_listing.models import Name
from .serializer import DataSerializer
# Create your views here.

@api_view(["GET"])
def getData(request):
    app = Name.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def postData(request):
    return Response