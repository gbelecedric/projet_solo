from django.db import models

# Create your models here.
class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True
        
class Link(Timemodels):
    facebook = models.URLField()
    twitter = models.URLField()
    intagrame = models.URLField()
    linkedin = models.URLField()
    youtube = models.URLField()
  
 
class Info(Timemodels):
    contact = models.IntegerField()
    residential = models.IntegerField()
    homes  = models.IntegerField()
    years = models.IntegerField()
    complains = models.IntegerField()
    offices = models.IntegerField()
    adrresse = models.CharField(max_length=250)
    maps = models.CharField(max_length=200)

    

