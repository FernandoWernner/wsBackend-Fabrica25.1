from rest_framework import serializers
from .models import Character, Episode

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class CharacterSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True) 

    class Meta:
        model = Character
        fields = '__all__'
