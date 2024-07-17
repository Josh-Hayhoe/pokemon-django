from django.urls import path
from . import views, views

urlpatterns = [
    path('', views.button, name="button"),
    path('fetch-pokemon/', views.fetch_pokemon, name="fetch_pokemon"),
]