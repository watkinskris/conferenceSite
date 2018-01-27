from django.db import models

class Awardnominee(models.Model):
    nominee_name = models.CharField(max_length=20)
    nominee_description = models.TextField()
    nominee_image_name = models.CharField(max_length=20)
    num_votes = models.SmallIntegerField()

    def __str__(self):
        return self.nominee_name