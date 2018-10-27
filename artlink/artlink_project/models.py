from django.db import models
from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify



    class Activity(models.Model):
        title = models.CharField(max_length=100, unique = True)
        features = models.CharField(max_length=128, unique = True)
        place = models.CharField(max_length=128, unique = True)
        cost = models.CharField(max_length=50, unique = True)
        contact = models.CharField(max_length=128, unique = True)
        welcomeComment = models.CharField(max_length=400, unique = True)
        webLink = models.CharField(max_length=128, unique = True)
        review  = models.foreignKeym(Review, on_delete = models.CASCADE)
        sense = models.ForeignKey(Sense, on_delete = models.CASCADE)
        description = models.CharField(max_length=400, unique = True)
        #url = models.FieldFile

        slug = models.SlugField(unique=True)


    def __str__(self):
        return self.title



    class Sense(models.Model):
        sense = models.CharField(max_length=10, unique = True)



    class Review(models.Model):
        review =  models.CharField(max_length=10, unique = True)
        name = models.CharField(max_length=128, unique = True)


    def __str__(self):
        return self.name


















