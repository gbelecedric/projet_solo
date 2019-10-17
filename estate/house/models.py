# Create your models here.
#--------------------import--blog-----------#
from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
# Create your models here.
#------------------------ blog_app_model --------------#
class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True

class Specification(Timemodels):
    titre =  models.CharField(max_length=255)
    
    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = 'specification'
        verbose_name_plural = 'specification'
        
class Vues(Timemodels):
    titre =  models.CharField(max_length=255)
    image = image= models.ImageField( upload_to='image_views')
    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = 'vues'
        verbose_name_plural = 'vues'

class Piscine(Timemodels):
    titre =  models.CharField(max_length=255)
    image = image= models.ImageField( upload_to='image_piscine')
    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = 'piscine'
        verbose_name_plural = 'piscine'

class Interior(Timemodels):
    titre =  models.CharField(max_length=255)
    image = image= models.ImageField( upload_to='image_interior')    
    def __str__(self):
        return self.titre
    class Meta:
        verbose_name = 'interior'
        verbose_name_plural = 'interieur maison'
 
class Video(Timemodels):
    thumb = models.ImageField( upload_to='thumb', verbose_name="image du haut", blank=True)
    lien = models.URLField(max_length=200 , blank=True)
    nom = models.CharField(max_length=50)
    video = models.FileField(upload_to="video" ,verbose_name="image du bas")


class Maison(Timemodels):
    nom =  models.CharField(max_length=255)
    description = models.TextField()
    image_principale = models.ImageField(upload_to ='image')
    vues = models.ForeignKey(Vues, related_name="vues", verbose_name="photo vue", on_delete=models.CASCADE, blank=True)
    interiors = models.ForeignKey(Interior, related_name="interieur", verbose_name="photo interieur", on_delete=models.CASCADE , blank=True)
    piscines = models.ForeignKey(Piscine, related_name="piscine" ,verbose_name="photo piscine", on_delete=models.CASCADE, blank=True)
    price = models.FloatField()
    lieu=  models.CharField(max_length=255)
    comming =  models.BooleanField(default=False)
    solde =  models.BooleanField(default=False)
    short = models.CharField(max_length=100, verbose_name="courte description",blank=True)
    size = models.PositiveIntegerField()
    Beds = models.PositiveIntegerField()
    Baths = models.PositiveIntegerField() 
    Garage = models.PositiveIntegerField()
    taxe_include = models.BooleanField(default=True)
    oreviews =  HTMLField('oreviviews',)
    specification = models.ManyToManyField(Specification)
    
    
     
    def __str__(self):
        
        return self.nom
    class Meta:
        verbose_name = 'maison'
        verbose_name_plural = 'nos maisons'
    

    
    
    