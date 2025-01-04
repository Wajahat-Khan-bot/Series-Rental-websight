from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Series(models.Model):
    title = models.CharField(max_length=100)
    daily_rate = models.FloatField()
    release_date = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    