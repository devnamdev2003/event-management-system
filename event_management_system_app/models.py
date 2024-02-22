from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    priority = models.IntegerField(default=1)
    description = models.TextField(default='')  # Add description field with default value
    location = models.CharField(max_length=255, default='')  # Add location field with default value
    organizer = models.CharField(max_length=100, default='')  # Add organizer field with default value
