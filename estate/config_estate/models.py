from django.db import models

# Create your models here.
class Timemodels(models.Model):
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    status =  models.BooleanField(default=True)
    
    class Meta:
        abstract=True
        
class Image(Timemodels):
    image = models.ImageField(upload_to="image")
    
    
    
class Background(Timemodels):
    about = models.ImageField(upload_to='abouts', )
    properti = models.ImageField(upload_to='property', )
    develop = models.ImageField(upload_to='develop', )
    contact = models.ImageField(upload_to='contact', )
    details = models.ImageField(upload_to='details', )
    new  = models.ImageField(upload_to='new', )
    category =  models.ImageField(upload_to='category', )

 
class Features (Timemodels):
    secure = models.CharField(max_length=250, verbose_name="secure area")
    eco= models.CharField(max_length=250, verbose_name="eco-friendly homes")
    parking = models.CharField(max_length=250, verbose_name="free parking")
    community = models.CharField(max_length=250 , verbose_name="comunity pool ")
    deal = models.CharField(max_length=250 , verbose_name="best deals")

class Home(Timemodels):
    interior = models.TextField(verbose_name="interior")
    envi = models.TextField(verbose_name="enviorment friendly")
    text = models.CharField(max_length=250 ,verbose_name="text de contact")
    
class Abouts(Timemodels):
    text = models.CharField(max_length=250 ,verbose_name="text du background")
    join = models.TextField(verbose_name="JOIN OUR TEAM")
    work = models.TextField(verbose_name="WORK REMOTE")
    text_slide = models.CharField(max_length=250 ,verbose_name="text a cote du slide ")
    image = models.ManyToManyField(Image, verbose_name="slide") 

class Development(Timemodels):
    text = models.CharField(max_length=250 ,verbose_name="text du background")
    titre = models.TextField(verbose_name="titre subscribe")
    text_slide = models.CharField(max_length=250 ,verbose_name="text de subscribe")
    
class News(Timemodels):
    text = models.CharField(max_length=250 ,verbose_name="text du background")

class Contact(Timemodels):
    text = models.CharField(max_length=250 ,verbose_name="text du background")
    
     
     
    
    
    

