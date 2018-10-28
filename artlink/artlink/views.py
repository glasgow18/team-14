from django.shortcuts import render
from artlink.forms import *
from artlink.search import normalize_query, get_query


def index(request):
    return render(request, 'index.html')


def add(request):
    return render(request, 'add.html')


def faq(request):
    return render(request, 'faq.html')


def about(request):
    return render(request, 'about.html')


def show_activity(request, activity_slug):
    # Assign aData to Activity object

    aData = Activity.objects.get(slug=activity_slug)
    context_dict = {"aData": aData}
    return render(request, 'activity.html', context=context_dict)


def submit_activity(request):
    # process form data only if it's a post request
    if request.method == 'POST':
        activity_form = SubmitActivityForm(data=request.POST)
        if activity_form.is_valid():
            activity = activity_form.save()
            return show_activity(request, activity.slug)
    else:
        activity_form = SubmitActivityForm()

    # TODO placeholder template: needs to be changed to submit_activity.html
    # DEBUG needed, submit form does not work with current models
    return render(request, 'add.html', {'activity_form': activity_form})


def browse(request):
    entry = None
    found_activities = None
    found = None
    query_string = ''
    # this is the data the search function will look through
    # TODO sense needs to be added to this, but this comes with debugging the model/choicefield add
    search_fields = ('title', 'features', 'welcomeComment', 'description')

    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry = get_query(query_string, search_fields)

        #Order the Activity objects found by order of id
        found_activities = Activity.objects.filter(entry).order_by('id')

        # only display activities if some are actually found
        found = found_activities.exists()

    return render(request, 'browse.html',
                  {'query_string': query_string, 'found': found, 'found_activities': found_activities})
