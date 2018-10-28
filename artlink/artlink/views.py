from django.shortcuts import render
from django.http import HttpResponse
from artlink.forms import *

def index(request):

    return render(request, 'index.html')


def add(request):


    return render(request, 'add.html')

def browse(request):


    return render(request, 'browse.html')

def about(request):


    return render(request, 'about.html')

def show_activity(request, activity_slug):
    return render(request, 'activity.html')

def submit_activity(request):
    # process form data only if it's a position
    if request.method == 'POST':
        activity_form = SubmitActivityForm(data=request.POST)
        if activity_form.is_valid():
            activity = activity_form.save()
            return show_activity(request, activity.slug)
    else:
        activity_form = SubmitActivityForm()

    # placeholder template: needs to be changed to submit_activity.html
    return render(request, 'add.html', {'activity_form': activity_form})
