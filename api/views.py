from django.shortcuts import render
from rest_framework import viewsets
from .models import Character,  Episode
from .serializers import CharacterSerializer, EpisodeSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    
def character_list(request):
    characters = Character.objects.all()
    return render(request, 'personagens.html', {'Personagens': characters})

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

