from django.db import models

# Create your models here.

class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True
        
class Poste(Timemodels):
    
    nom = models.CharField(max_length=160)
        
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name = 'Poste'
        verbose_name_plural = 'Postes'

class Personnel(Timemodels):
    nom = models.CharField(max_length=160)
    descriptions = models.TextField()
    photo = models.ImageField(upload_to='photo_presonnel')
    poste = models.ForeignKey(Poste, on_delete=models.CASCADE,related_name="poste_presonnel")

    def __str__(self):
        return self.nom+ " " + self.poste.nom

    class Meta:
        verbose_name = 'salarié'
        verbose_name_plural = 'salarié'
