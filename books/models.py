from django.db import models

# Create your books here.
class Book(models.Model):
    # each class variable represents a database i.e. table field in the model
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=30)
    release_date = models.DateTimeField('release date')
    genre = models.CharField(max_length=200)
