from django import forms
from django.forms import ModelForm, TextInput

from .models import Search, Player, Team, Coach, Game, Highlight
from django.contrib.auth.models import User


class SearchCreateForm(ModelForm):
    class Meta:
        model = Search
        fields = ['player_lname',
        'player_position', 'highlight_type']

    def __init__(self, *args, **kwargs):
        super(SearchCreateForm, self).__init__(*args, **kwargs)
