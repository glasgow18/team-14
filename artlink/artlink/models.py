from django.db import models
from django.contrib import admin
from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
import uuid


#class Review(models.Model):
 #   review =  models.TextField(blank=True)
 #   name = models.CharField(max_length=60, unique= True)

  #  def __str__(self):
   #     return self.name


class Sense(models.Model):
    sense = models.CharField(max_length=10, unique= True)

    def __str(self):
        return self.sense


class Activity(models.Model):
    title = models.CharField(max_length=100, unique=True)
    features = models.TextField()
    place = models.CharField(max_length=128, unique=False)
    cost = models.CharField(max_length=50, unique=False)
    contact = models.CharField(max_length=128, unique=False)
    welcomeComment = models.TextField(blank=False)
    webLink = models.CharField(max_length=128, unique=False)
    #review = models.ForeignKey(Review, on_delete=models.CASCADE)
    sense = models.ForeignKey(Sense, on_delete=models.CASCADE)
    description = models.TextField()

    slug = models.SlugField(unique=True,default=uuid.uuid1)

    def __str__(self):
        self.slug = slugify(self.title)
        return self.title
