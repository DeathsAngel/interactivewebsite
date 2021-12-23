# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-22 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipeName', models.TextField(default='')),
                ('recipeIngredients', models.TextField(default='')),
                ('recipeDirections', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personName', models.TextField(default='')),
                ('password', models.TextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='Name',
        ),
    ]