from django.db import models

from django.utils import timezone



class Book(models.Model):

  title = models.CharField(max_length=200)

  author = models.CharField(max_length=100)

  publish_date = models.DateField(default=timezone.now)

  isbn = models.CharField(max_length=13, unique=True)

  page_count = models.IntegerField()

  description = models.TextField(blank=True)



  def __str__(self):

    return self.title