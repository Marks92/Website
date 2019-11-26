from django import forms
from django.forms import ModelForm
from .models import Games

class Game_Form(forms.Form):
    class Meta:
        model = Games
        fields = ['game_name']