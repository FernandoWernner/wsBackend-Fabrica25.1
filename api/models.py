from django.db import models

class Episode(models.Model):
    name = models.CharField(max_length=255)
    air_date = models.DateField()
    episode_code = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    species = models.CharField(max_length=100)
    image = models.URLField()
    episodes = models.ManyToManyField(Episode) 

    def __str__(self):
        return self.name

