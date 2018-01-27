from django import forms
from django.forms import ModelForm
from registrant.models import Registrant
from django.core.validators import RegexValidator

MISTER = 'Mr.'
MISS = 'Ms.'
MISSUS = 'Mrs.'
DOCTOR = 'Dr.'
MEALPACK = 'MP'
DAY2DINNER = 'D2D'
MASTERCARD = 'MC'
VISA = 'VS'
AMERICAN_EXPRESS = 'AM'
SOCIAL_NETWORKS = 'SN'
AUTOMOBILE_MEDIA = 'AM'
DIGITAL_IMAGES = 'DI'
PHYSICAL_LAYER = 'PL'
MACHINE_LEARNING = 'ML'
BIOMETRICS = 'SB'
INCIDENT_RESPONSE = 'IS'
INCIDENT_ID = 'II'
TEAM_MANAGEMENT = 'TM'
SEVENTEEN = '2017'
EIGHTEEN = '2018'
NINETEEN = '2019'
TWENTY = '2020'
TWENTYONE = '2021'
TWENTY_TWO = '2022'
JANUARY = '01'
FEBRUARY = '02'
MARCH = '03'
APRIL = '04'
MAY = '05'
JUNE = '06'
JULY = '07'
AUGUST = '08'
SEPTEMBER ='09'
OCTOBER = '10'
NOVEMBER = '11'
DECEMBER = '12'

ALABAMA = 'AL'
ALASKA = 'AK'
ARIZONA = 'AZ'
ARKANSAS = 'AR'
CALIFORNIA = "CA"
COLORADO = 'CO'
CONNECTICUT = 'CT'
DELAWARE = 'DE'
DISTRICT_OF_COLUMBIA = 'DC'
FLORIDA = 'FL'
GEORGIA = 'GA'
HAWAII = "HI"
IDAHO = "ID"
ILLINOIS = "IL"
INDIANA = "IN"
IOWA = "IA"
KANSAS = "KS"
KENTUCKY = "KY"
LOUISIANA = "LA"
MAINE = "ME"
MARYLAND = "MD"
MASSACHUSETTS = "MA"
MICHIGAN = "MI"
MINNESOTA = "MN"
MISSISSIPPI = "MS"
MISSOURI = "MO"
MONTANA = "MT"
NEBRASKA = "NE"
NEVADA = "NV"
NEW_HAMPSHIRE = "NH"
NEW_JERSEY = "NJ"
NEW_MEXICO = "NM"
NEW_YORK = "NY"
NORTH_CAROLINA = "NC"
NORTH_DAKOTA = "ND"
OHIO = "OH"
OKLAHOMA = "OK"
OREGON = "OR"
PENNSYLVANIA = "PA"
RHODE_ISLAND = "RI"
SOUTH_CAROLINA = "SC"
SOUTH_DAKOTA = "SD"
TENNESSE = "TN"
TEXAS = "TX"
UTAH = "UT"
VERMONT = "VT"
VIRGINIA = "VA"
WASHINGTON = "WA"
WEST_VIRGINIA = "WV"
WISCONSIN = "WI"
WYOMING = "WY"
AMERICAN_SAMOA = "AS"
GUAM = "GU"
NORTHERN_MARIANA_ISLANDS = "MP"
PUERTO_RICO = "PR"
MINOR_OUTLYING_ISLANDS = "UM"
VIRGIN_ISLANDS = "VI"
ARMED_FORCES_AMERICAS = "AA"
ARMED_FORCES_PACIFIC = "AP"
ARMED_FORCES_OTHERS = "AE"

STATE_CHOICES = (
    (ALABAMA, 'Alabama'),
    (ALASKA, 'Alaska'),
    (ARIZONA, 'Arizona'),
    (ARKANSAS, 'Arkansas'),
    (CALIFORNIA, 'California'),
    (COLORADO, 'Colorado'),
    (CONNECTICUT, 'Connecticut'),
    (DELAWARE, 'Delaware'),
    (DISTRICT_OF_COLUMBIA, 'D.C.'),
    (FLORIDA, 'Florida'),
    (GEORGIA, 'Georgia'),
    (HAWAII, 'Hawaii'),
    (IDAHO, 'Idaho'),
    (ILLINOIS, 'Illinois'),
    (INDIANA, 'Indiana'),
    (IOWA, 'Iowa'),
    (KANSAS, 'Kansas'),
    (KENTUCKY, 'Kentucky'),
    (LOUISIANA, 'Louisiana'),
    (MAINE, 'Maine'),
    (MARYLAND, 'Maryland'),
    (MASSACHUSETTS, 'Massachusetts'),
    (MICHIGAN, 'Michigan'),
    (MINNESOTA, 'Minnesota'),
    (MISSISSIPPI, 'Mississippi'),
    (MISSOURI, 'Missouri'),
    (MONTANA, 'Montana'),
    (NEBRASKA, 'Nebraska'),
    (NEVADA, 'Nevada'),
    (NEW_HAMPSHIRE, 'New Hampshire'),
    (NEW_JERSEY, 'New Jersey'),
    (NEW_MEXICO, 'New Mexico'),
    (NEW_YORK, 'New York'),
    (NORTH_CAROLINA, 'North Carolina'),
    (NORTH_DAKOTA, 'North Dakota'),
    (OHIO, 'Ohio'),
    (OKLAHOMA, 'Oklahoma'),
    (OREGON, 'Oregon'),
    (PENNSYLVANIA, 'Pennsylvania'),
    (RHODE_ISLAND, 'Rhode Island'),
    (SOUTH_CAROLINA, 'South Carolina'),
    (SOUTH_DAKOTA, 'South Dakota'),
    (TENNESSE, 'Tennessee'),
    (TEXAS, 'Texas'),
    (UTAH, 'Utah'),
    (VERMONT, 'Vermont'),
    (VIRGINIA, 'Virginia'),
    (WASHINGTON, 'Washington'),
    (WEST_VIRGINIA, 'West Virginia'),
    (WISCONSIN, 'Wisconsin'),
    (WYOMING, 'Wyoming'),
    (AMERICAN_SAMOA, 'American Samoa'),
    (GUAM, 'Guam'),
    (NORTHERN_MARIANA_ISLANDS, 'Northern Mariana Islands'),
    (PUERTO_RICO, 'Puerto Rico'),
    (MINOR_OUTLYING_ISLANDS, 'United States Minor Outlying Islands'),
    (VIRGIN_ISLANDS, 'Virgin Islands'),
    (ARMED_FORCES_AMERICAS, 'Armed Forces Americas'),
    (ARMED_FORCES_PACIFIC, 'Armed Forces Pacific'),
    (ARMED_FORCES_OTHERS, 'Armed Forces Others'),
)

TITLE_CHOICES = (
    (MISTER, 'Mr.'),
    (MISS, 'Ms.'),
    (MISSUS, 'Mrs.'),
    (DOCTOR, 'Dr.'),
)

MEAL_CHOICES = (
    (MEALPACK, 'Dinner Both Days'),
    (DAY2DINNER, 'Day 2 Dinner Only'),
)

CARD_CHOICES = (
    (MASTERCARD, 'Master Card'),
    (VISA, 'Visa'),
    (AMERICAN_EXPRESS, 'American Express'),
)

SESSION1_CHOICES = (
    (SOCIAL_NETWORKS, 'Verifying Information on Social Networks'),
    (AUTOMOBILE_MEDIA, 'Investigations Involving Automobile Media'),
    (DIGITAL_IMAGES, 'Authentication of Digital Images'),
)

SESSION2_CHOICES = (
    (PHYSICAL_LAYER, 'Physical Layer Security'),
    (MACHINE_LEARNING, 'Machine Learning: Security'),
    (BIOMETRICS, 'Security of Biometrics'),
)

SESSION3_CHOICES = (
    (INCIDENT_RESPONSE, 'Digital Forensics: Incident Response'),
    (INCIDENT_ID, 'Identification and Authentication of Incidents'),
    (TEAM_MANAGEMENT, 'Management of the Incident Response Team'),
)

EXPIRATION_YEAR_CHOICES = (
    (SEVENTEEN, '2017'),
    (EIGHTEEN, '2018'),
    (NINETEEN, '2019'),
    (TWENTY, '2020'),
    (TWENTYONE, '2021'),
    (TWENTY_TWO, '2022'),
)
EXPIRATION_MONTH_CHOICES = (
    (JANUARY, '01'),
    (FEBRUARY, '02'),
    (MARCH, '03'),
    (APRIL, '04'),
    (MAY, '05'),
    (JUNE, '06'),
    (JULY, '07'),
    (AUGUST, '08'),
    (SEPTEMBER, '09'),
    (OCTOBER, '10'),
    (NOVEMBER, '11'),
    (DECEMBER, '12'),
)


class RegistrationForm(ModelForm):
    class Meta:
        model = Registrant
        fields = (
            'title',
            'firstname',
            'lastname',
            'address1',
            'address2',
            'city',
            'state',
            'zipcode',
            'telephone',
            'email',
            'company',
            'website',
            'position',
            'meals',
            'billing_firstname',
            'billing_lastname',
            'card_type',
            'card_number',
            'card_csv',
            'exp_year',
            'exp_month',
            'session1',
            'session2',
            'session3'
        )

        widgets = {
            'title': forms.Select(choices=TITLE_CHOICES),
            'state': forms.Select(choices=STATE_CHOICES),
            'meals': forms.Select(choices=MEAL_CHOICES),
            'card_type': forms.Select(choices=CARD_CHOICES),
            'exp_year': forms.Select(choices=EXPIRATION_YEAR_CHOICES),
            'exp_month': forms.Select(choices=EXPIRATION_MONTH_CHOICES),
            'session1': forms.RadioSelect(choices=SESSION1_CHOICES),
            'session2': forms.RadioSelect(choices=SESSION2_CHOICES),
            'session3': forms.RadioSelect(choices=SESSION3_CHOICES),
        }
        required = {
            'address2': False,
            'meals': False,
            'website': False,
        }

        validators = {
            'telephone': [RegexValidator(regex='^[0-9]{3}\-[0-9]{3}\-[0-9]{4}$',
                                        message= 'Telephone entered is not in the correct format of 123-123-1234.',
                                        code='invalid_phonenumber'),
                          ],
            'card_number': [RegexValidator(regex='^[0-9]{16}$',
                                        message= 'Card Number must be 16 digits long',
                                        code='invalid_cardnumber'),
                            ],
            'card_csv': [RegexValidator(regex='^{0-9]{4}$',
                                        message='CSV must be 4 digits and can be found on the back on the card',
                                        code='invalid_csv'),
                           ],
        }






