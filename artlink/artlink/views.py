from django.shortcuts import render
from django.http import HttpResponse
from artlink.forms import *
from artlink.search import normalize_query, get_query

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

def browse(request):
    entry = None
    found_activities = None
    found = None
    query_string = ''
    search_fields = ('title', 'features', 'welcomeComment', 'description')

    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry = get_query(query_string, search_fields)
        found_activities = Activity.objects.filter(entry).order_by('id')

        found = found_activities.exists()

    return render(request, 'browse.html', {'query_string': query_string, 'found': found, 'found_activities': found_activities})
