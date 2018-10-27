from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def add(request):


    return render(request, 'templates/add.html')

def browse(request):


    return render(request, 'templates/browse.html')

def about(request):


    return render(request, 'about.html')

def activity_show(request, activity_slug):


    return render(request, 'templates/category.html')
