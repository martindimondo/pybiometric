from django.db import models


class BigramTime(models.Model):
    user = models.ForeignKey('auth.User')
    chars = models.CharField(max_length=2)
    duration = models.IntegerField()


class KeystrokeTime(models.Model):
    user = models.ForeignKey('auth.User')
    char = models.CharField(max_length=1)
    duration = models.IntegerField()
