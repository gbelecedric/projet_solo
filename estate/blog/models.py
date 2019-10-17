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

    
class Tag(Timemodels):
    nom = models.CharField(max_length=225)
    
    def __str__(self):
        return self.nom

class Categorie(Timemodels):
    titre =  models.CharField(max_length=255)
    image = models.ImageField(upload_to='categorie', blank=True)
    nom =  models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titre
    
    
    
class Article(Timemodels):
    titre =  models.CharField(max_length=255)
    description = models.TextField()
    categorie_id =  models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name="categorie")
    contenu =  HTMLField('article_description',)
    photo = models.ImageField(upload_to ='article')
    tag_name = models.ManyToManyField(Tag)
    nom =  models.ForeignKey(User,on_delete=models.CASCADE)
    nbr_comment = models.IntegerField(blank=True,default="0")
    
    def __str__(self):
        
        return self.titre
    
    
class Commentaire(Timemodels):
    article_id =  models.ForeignKey(Article,on_delete=models.CASCADE, related_name="article_poster")
    username = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.URLField(max_length=250)
    contenu =  models.TextField(null=True)
    image= models.ImageField( upload_to='image_comment',)
    
    def __str__(self):
        return self.username
    
class Reply(Timemodels):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(max_length=250)
    comment = models.ForeignKey(Commentaire,on_delete=models.CASCADE, related_name="reponse")
    contenu =  models.TextField()
    image= models.ImageField( upload_to='image_comment')
    
    def __str__(self):
        return self.nom
    
    
