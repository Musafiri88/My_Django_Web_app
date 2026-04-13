from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Band(models.Model):
    '''Model representing a band.'''
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    biography = models.TextField()
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)])
    active = models.BooleanField(default=True)
    official_homepage = models.URLField()
