# Generated by Django 2.0 on 2017-12-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Mr.', 'Mr.'), ('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.')], default='Mr.', max_length=4)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'D.C.'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'), ('AS', 'American Samoa'), ('GU', 'Guam'), ('MP', 'Northern Mariana Islands'), ('PR', 'Puerto Rico'), ('UM', 'United States Minor Outlying Islands'), ('VI', 'Virgin Islands'), ('AA', 'Armed Forces Americas'), ('AP', 'Armed Forces Pacific'), ('AE', 'Armed Forces Others')], default='AL', max_length=2)),
                ('zipcode', models.CharField(max_length=5)),
                ('telephone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.CharField(blank=True, max_length=50)),
                ('position', models.CharField(max_length=30)),
                ('company', models.CharField(max_length=30)),
                ('meals', models.CharField(blank=True, choices=[('mealpack', 'Dinner Both Days'), ('dinnerday2', 'Day 2 Dinner Only')], max_length=3, null=True)),
                ('billing_firstname', models.CharField(max_length=20)),
                ('billing_lastname', models.CharField(max_length=20)),
                ('card_type', models.CharField(choices=[('MC', 'Master Card'), ('VS', 'Visa'), ('AM', 'American Express')], default='VS', max_length=2)),
                ('card_number', models.CharField(max_length=16)),
                ('card_csv', models.CharField(max_length=4)),
                ('exp_year', models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022')], default='2017', max_length=4)),
                ('exp_month', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12')], default='01', max_length=2)),
                ('session1', models.CharField(choices=[('Workshop A', 'Verifying Information on Social Networks'), ('Workshop B', 'Investigations Involving Automobile Media'), ('Workshop C', 'Authentication of Digital Images')], default='', max_length=20)),
                ('session2', models.CharField(choices=[('Workshop D', 'Physical Layer Security'), ('Workshop E', 'Machine Learning: Security'), ('Workshop F', 'Security of Biometrics')], default='', max_length=20, null=True)),
                ('session3', models.CharField(choices=[('Workshop G', 'Digital Forensics: Incident Response'), ('Workshop H', 'Identification and Authentication of Incidents'), ('Workshop I', 'Management of the Incident Response Team')], default='', max_length=20)),
                ('date_of_registration', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
