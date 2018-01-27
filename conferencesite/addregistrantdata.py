from registrant.models import Registrant
import json


class Register(dict):
    _keys = ['title', 'firstname', 'lastname', 'address1', 'address2', 'city', 'state', 'zipcode', 'telephone', 'email',
             'company', 'position', 'website', 'billing_firstname', 'billing_lastname', 'card_type', 'card_number',
             'card_csv', 'exp_month', 'exp_year', 'meals', 'session1', 'session2', 'session3', 'date_of_registration']

    def __init__(self, registrant):
        for key in self._keys:            # loop through the keys and set each key to its value
            self[key] = registrant[key]   # this instances key:value should be set to the entered registrants key:value


with open('registrants.json') as registrantData:

    dataObject = json.load(registrantData)  # load in the registrant data from the JSON file

    # for each object in the list with key registrants, create a new Registrant object and add it to a list of objects
    for person in dataObject['registrants']:
        r = Registrant(**person)
        r.save()





