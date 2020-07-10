import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
# Create your models here.

class Player(models.Model):
    id  = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField(default=timezone.now)
    position = models.CharField(max_length=25)
    def __str__(self):
        return self.last_name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    home_arena = models.CharField(max_length=35)
    def __str__(self):
        return self.name

class Coach(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.last_name

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    game_date = models.DateTimeField(default=timezone.now)
    arena = models.CharField(max_length=35)
    game_type = models.CharField(max_length=25)
    home_team = models.CharField(max_length=35)
    away_team = models.CharField(max_length=35)
    def __str__ (self):
        return self.game_date

class Highlight(models.Model):
    highlight_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, default=1, on_delete=models.SET_DEFAULT)
    player_id = models.ForeignKey(Player, default=1, on_delete=models.SET_DEFAULT)
    #c_tp_id = models.ForeignKey(CoachTimePeriod, default=1, on_delete=models.SET_DEFAULT)
    highlight_type = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return self.highlight_type

class Search(models.Model):
    player_lname = models.CharField(max_length=41, null=True, blank=True)
    player_position = models.CharField(max_length=25, null=True, blank=True)
    highlight_type = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.player_lname
        
    def search_highlight(cls, player_lname, player_position, highlight_type):
        search_results = cls(player_lname=player_lname,
        player_position=player_position, highlight_type=highlight_type)
        return search_results