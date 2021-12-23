from django.db import models

class List(models.Model):
    pass

class user(models.Model):
    personName = models.TextField(default='')
    password = models.TextField(default='')

class recipe(models.Model):
    recipeName = models.TextField(default='')
    recipeIngredients = models.TextField(default='')
    recipeDirections = models.TextField(default='')
    list = models.ForeignKey(List, default=None)