from django.db import models



class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    # Add other event fields as per your requirements


class Report(models.Model):
    title = models.CharField(max_length=100)
    # Add other report fields as per your requirements