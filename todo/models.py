from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name