from django.db import models

# Create your models here.

class Url(models.Model):
    #~database = 2 tables (link, uuid)
    link = models.CharField(max_length=1000)
    uuid = models.CharField(max_length=10)
