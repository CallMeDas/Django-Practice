from django.db import models


class service (models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

# Create your models here.
 