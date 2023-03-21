from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    date = models.DateTimeField('date published')
    description = models.TextField()
