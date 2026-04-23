from django.db import models

# Create your models here.
class Esp32_data(models.Model):
    cas = models.DateTimeField(auto_now_add = True)
    teplota = models.FloatField()
    svetlo = models.FloatField()