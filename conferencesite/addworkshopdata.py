from workshop.models import Workshop
import json

with open('workshopDetails.json') as workshopData:

    dataObject = json.load(workshopData)  # load in the registrant data from the JSON file

    # for each object in the list with key registrants, create a new Registrant object and add it to a list of objects
    for workshop in dataObject['workshops']:
        r = Workshop(**workshop)
        r.save()