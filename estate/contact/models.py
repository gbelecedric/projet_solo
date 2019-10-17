from django.db import models


class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True


class Message(Timemodels):
    
    nom = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
      

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Newsletter(Timemodels):
    email = models.EmailField()

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'

    def __str__(self):
        return self.email