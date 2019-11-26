from __future__ import unicode_literals

from django.db import models

# Create your models here.`>

class People(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    age = models.IntegerField()

class Genres(models.Model):
    genre_type = models.CharField(max_length=100)

class Games(models.Model):
    game_genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.game_genre}  {self.game_name}"

