from django.db import models

# Create your models here.

class Bitcoin(models.Model):
    timestamp = models.DateTimeField
    price = models.FloatField
