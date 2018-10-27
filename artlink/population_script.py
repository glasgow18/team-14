# Populate local database with sample data
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","artlink_project.settings")

import django
django.setup()

from artlink.models import *
print("hie")
def populate():

    # Load sample data from files
    with open("population_data.json", "r") as f:
        activities = json.loads("".join(f.readlines()))
    # Populate database with data



    senses = ["Sound","Smell","Sight","Touch","Taste"]
    for s in senses:
        add_senses(s)

    for a in activities:
        add_activity(a)

    print("Population successful!")


def add_activity(activity):
    # This will throw a RuntimeWarning during population, which can be ignored for now.
    a = Activity.objects.get_or_create(title=activity["title"],description = activity["description"],features= activity["features"],place = activity["place"],cost= activity["cost"],contact= activity["contact"],welcomeComment= activity["welcomeComment"],webLink = activity["webLink"],review = Review.objects.get(review =activity["review"]),sense=Sense.objects.get(sense=activity["sense"]))[0]
    a.save()
    print("Activity added: %s" % e.title)


def add_senses(sense):
    s = Sense.objects.get_or_create(sense = sense)
    s.save()
    print("Sense added %s" % s.sense)


if __name__ == "__main__":
    print("Starting population script for artlink")
    populate()
