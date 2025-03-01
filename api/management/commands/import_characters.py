import requests
from django.core.management.base import BaseCommand
from api.models import Character

class Command(BaseCommand):
    help = 'Importa personagens da API Rick & Morty'

    def handle(self, *args, **kwargs):
        url = "https://rickandmortyapi.com/api/Personagens"
        response = requests.get(url)
        data = response.json()

        for character in data["results"]:
            Character.objects.create(
                name=character["name"],
                status=character["status"],
                species=character["species"],
                image=character["image"]
            )

        self.stdout.write(self.style.SUCCESS('Sucesso na importação dos personagens!'))