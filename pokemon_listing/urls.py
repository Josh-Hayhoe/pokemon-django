from django.urls import path
from . import views, views as main_views

urlpatterns = [
    path('', main_views.button, name="button"),
    path('fetch-pokemon/', views.fetch_pokemon, name="fetch_pokemon")
]