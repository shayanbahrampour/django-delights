from dataclasses import fields
from statistics import mode
from django import forms
from .models import Ingredient, MenuItem


class MenuUpdateForm(forms.ModelForm):

    class Meta:
        model = MenuItem
        fields=("name","price","ingredient")
    

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields=("name","price","quantity","unit")