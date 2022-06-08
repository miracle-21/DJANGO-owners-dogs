from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=300)
    age = models.IntegerField(default = '0')
    class Meta:
        db_table = 'owners'

class Dog(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default = '0')
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    class Meta:
        db_table = 'dogs'