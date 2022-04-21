from pyexpat import model
from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.


class Ingredient(models.Model):
    WEIGHT_CHOICES =[
        ("L","lbs"),
        ("P","pnds"),
        ("G","grams")
    ]
    name = models.CharField(max_length=25)
    price = models.FloatField()
    quantity = models.FloatField()
    unit = models.CharField(max_length=1,choices=WEIGHT_CHOICES)
    def get_absolute_url(self):
        return ""


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    ingredient = models.ManyToManyField(Ingredient)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return ""

