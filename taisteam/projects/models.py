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
        return self.notification


class LettersTais(models.Model):
    notification = models.CharField(max_length=10)
    theme = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    to_whom = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-notification']


    def __str__(self):
        return self.notification


class LettersTeks(models.Model):
    notification = models.CharField(max_length=10)
    theme = models.CharField(max_length=100)
    content = models.CharField(max_length=255)
    to_whom = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True)
    worker = models.CharField(max_length=30)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-notification']


    def __str__(self):
        return self.notification