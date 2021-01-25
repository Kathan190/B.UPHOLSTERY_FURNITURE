from django.db import models

# Create your models here.

class Sofa(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/image',default='')
    description = models.CharField(max_length=1000)
    

    def __str__(self):
        return self.name

class Beds(models.Model):
    name = models.CharField(max_length=200, null=True,default='')
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to='media/image',default='')
    description = models.CharField(max_length=1000,default='')

    def __str__(self):
        return self.name

class Chest(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/image',default='')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Dining(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/image',default='')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
    
class Dressing(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/image',default='')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Wardrobs(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media/image',default='')
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Index(models.Model):
    name = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + self.subject

class Images(models.Model):
    name = models.CharField(max_length=100, null=True)
    image1 = models.ImageField(upload_to='media/image', default='')
    image2 = models.ImageField(upload_to='media/image', default='')
    image3 = models.ImageField(upload_to='media/image', default='')

    def __str__(self):
        return self.name 

class Temp(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name