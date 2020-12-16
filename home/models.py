from django.db import models

# Create your models here.

class Sofa(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name