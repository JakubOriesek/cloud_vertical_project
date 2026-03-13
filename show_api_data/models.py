from django.db import models

class Pocasie(models.Model):
    cas = models.DateTimeField()          # čas merania
    teplota = models.FloatField()
    vietor = models.FloatField()
    vlhkost = models.FloatField()
    tlak = models.FloatField()
    o3 = models.FloatField()
    pocet = models.IntegerField()

# Create your models here.
