from django.db import models

# Create your models here.

class Sofa(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Beds(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Chest(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Dining(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Dressing(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Wardrobs(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name