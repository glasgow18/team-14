from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def add(request):


    return render(request, 'artlink/add.html')

def browse(request):


    return render(request, 'artlink/browse.html')

def about(request):


    return render(request, 'artlink/about.html')

def activity_show(request, activity_slug):


    return render(request, 'artlink/category.html')
