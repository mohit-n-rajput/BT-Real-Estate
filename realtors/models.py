from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    ''' When some field is optinal we use blank=True.'''
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_rvp = models.BooleanField(default=False) # realtor of the month field
    hire_date = models.DateTimeField(default=datetime.now, blank=True) 
    
    def __str__(self):
        return self.name