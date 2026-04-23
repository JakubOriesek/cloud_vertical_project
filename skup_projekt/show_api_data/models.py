from django.db import models

class Pocasie(models.Model):
    cas = models.DateTimeField()
    teplota = models.FloatField()
    tlak = models.FloatField()
    vietor = models.FloatField()
    o3 = models.FloatField()
    vlhkost = models.FloatField()
    pocet = models.IntegerField()

# Create your models here.
