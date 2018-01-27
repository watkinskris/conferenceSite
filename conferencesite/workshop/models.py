from django.db import models

class Workshop(models.Model):
    workshop_name = models.CharField(max_length=50)
    speaker_name = models.CharField(max_length=50)
    session_num = models.SmallIntegerField()
    room_num = models.CharField(max_length=5)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return self.workshop_name