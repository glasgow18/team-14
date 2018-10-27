from django.db import models
from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify


class Review(models.Model):
    review =  models.TextField(blank=True)
    name = models.CharField(max_length=60, unique= True)

    def __str__(self):
        return self.name


class Sense(models.Model):
    sense = models.CharField(max_length=10, unique= True)


class Activity(models.Model):
    title = models.CharField(max_length=100, unique=True)
    features = models.TextField()
    place = models.CharField(max_length=128, unique=True)
    cost = models.CharField(max_length=50, unique=True)
    contact = models.CharField(max_length=128, unique=True)
    welcomeComment = models.TextField(blank=True)
    webLink = models.CharField(max_length=128, unique=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    sense = models.ForeignKey(Sense, on_delete=models.CASCADE)
    description = models.TextField()

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
