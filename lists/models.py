from django.db import models

class Name(models.Model):
    personName = models.TextField(default='')
