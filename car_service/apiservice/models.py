from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    archived = models.BooleanField(default=False)
