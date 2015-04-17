from django.db import models

# Create your models here.

class Urls(models.Model):
    larga = models.CharField(max_length=32)
