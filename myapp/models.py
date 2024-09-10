from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    autor = models.CharField(max_length=200)
    published_date = models.DateTimeField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    cover = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=50)


    def __str__(self):
        return self.title

