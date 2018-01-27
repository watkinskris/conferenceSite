from django.db import models

class Registrant(models.Model):
    MISTER = 'Mr.'
    MISS = 'Ms.'
    MISSUS = 'Mrs.'
    DOCTOR = 'Dr.'
    MEALPACK = 'mealpack'
    DAY2DINNER = 'dinnerday2'
    MASTERCARD = 'MC'
    VISA = 'VS'
    AMERICAN_EXPRESS = 'AM'
    SOCIAL_NETWORKS = 'Workshop A'
    AUTOMOBILE_MEDIA = 'Workshop B'
    DIGITAL_IMAGES = 'Workshop C'
    PHYSICAL_LAYER = 'Workshop D'
    MACHINE_LEARNING = 'Workshop E'
    BIOMETRICS = 'Workshop F'
    INCIDENT_RESPONSE = 'Workshop G'
    INCIDENT_ID = 'Workshop H'
    TEAM_MANAGEMENT = 'Workshop I'
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

    title = models.CharField(max_length=4, choices=TITLE_CHOICES, default=MISTER)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, default=ALABAMA)
    zipcode = models.CharField(max_length=5)
    telephone = models.CharField(max_length=12)
    email = models.EmailField()
    website = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    meals = models.CharField(max_length=15, choices=MEAL_CHOICES, blank=True)
    billing_firstname = models.CharField(max_length=20)
    billing_lastname = models.CharField(max_length=20)
    card_type = models.CharField(max_length=2, choices=CARD_CHOICES, default=VISA)
    card_number = models.CharField(max_length=16)
    card_csv = models.CharField(max_length=4)
    exp_year = models.CharField(max_length=4, choices=EXPIRATION_YEAR_CHOICES, default=SEVENTEEN)
    exp_month = models.CharField(max_length=2, choices=EXPIRATION_MONTH_CHOICES, default=JANUARY)
    session1 = models.CharField(max_length=20, choices=SESSION1_CHOICES, default=None)
    session2 = models.CharField(max_length=20, choices=SESSION2_CHOICES, blank=True, default=None)
    session3 = models.CharField(max_length=20, choices=SESSION3_CHOICES, default=None)
    date_of_registration = models.DateField(null=True, blank=True)

    def __str__(self):
        return '%s %s %s %s' %(self.firstname, self.lastname, self.address1, self.city)



