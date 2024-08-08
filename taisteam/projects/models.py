from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)