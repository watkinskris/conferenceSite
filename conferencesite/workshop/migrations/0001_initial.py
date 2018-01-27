# Generated by Django 2.0 on 2017-12-18 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_name', models.CharField(max_length=50)),
                ('speaker_name', models.CharField(max_length=50)),
                ('session_num', models.SmallIntegerField()),
                ('room_num', models.CharField(max_length=5)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]
