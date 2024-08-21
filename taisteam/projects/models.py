from django.db import models

class Notice(models.Model):
    notification = models.CharField(max_length=11)
    about = models.CharField(max_length=255)
    theme = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    in_archive = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-notification']


    def __str__(self):
        return self.title


class LettersTais(models.Model):
    notification = models.CharField(max_length=11)
    about = models.CharField(max_length=255)
    theme = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    in_archive = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)