from awardnominee.models import Awardnominee
import json

with open('awardNominee.json') as awardData:

    dataObject = json.load(awardData)  # load in the registrant data from the JSON file

    # for each object in the list with key registrants, create a new Registrant object and add it to a list of objects
    for nominee in dataObject['nominees']:
        r = Awardnominee(**nominee)
        r.save()