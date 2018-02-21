from django.db import models

# Create your models here.
class Restaurant(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    zoom = models.PositiveIntegerField(default=14)
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title