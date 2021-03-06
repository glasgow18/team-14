# Populate local database with sample data
import json
import os
from django.db.utils import OperationalError
os.environ.setdefault("DJANGO_SETTINGS_MODULE","artlink_project.settings")

import django
django.setup()

from artlink.models import *


def populate():

    # Load sample data from json file
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
    # DEBUG @Sam: is this still actually the case?
     a, created = Activity.objects.get_or_create(title=activity["title"],description = activity["description"],features= activity["features"],place = activity["place"],cost= activity["cost"],contact= activity["contact"],welcomeComment= activity["welcomeComment"],webLink = activity["webLink"],sense=Sense.objects.get(sense=activity["sense"]))
     print("Activity added: %s" % a.title)


def add_senses(sense):
    s, created = Sense.objects.get_or_create(sense = sense)
    print("Sense added %s" % s.sense)


if __name__ == "__main__":
    print("Starting population script for artlink")
    populate()
