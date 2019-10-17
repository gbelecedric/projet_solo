from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from entreprise.models import * 
from config_estate.models import * 
from contact.models import * 
from blog.models import * 
from house.models import * 
from team.models import * 
#----------------------blog----------------#
class CommentaireSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = Commentaire
        fields = '__all__'
        depth = 2

class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    article_poster = CommentaireSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'
        depth = 2

class CategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    categorie = ArticleSerializer(read_only=True ,many=True)
    
    class Meta:
        model = Categorie
        fields = '__all__'
        depth = 1
class TagSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    tag_name = ArticleSerializer(read_only=True ,many=True)
    
    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1
#------------------------------------------endblog-------------------~##-~###
#---------------------------contact------------------------------~##


class NewsletterSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
  
    
    class Meta:
        model = Newsletter
        fields = '__all__'
        depth = 1
class MessageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = Message
        fields = '__all__'
        depth = 1
        
        
#------------------entreprise--------------------------#
class InfoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
      
    
    class Meta:
        model = Info
        fields = '__all__'
        depth = 1
class LinkSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = Link
        fields = '__all__'
        depth = 1
#--------------------house-------------------------------#
class  MaisonSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model =  Maison
        fields = '__all__'
        depth = 2
class VideoSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
   
    class Meta:
        model = Video
        fields = '__all__'
        depth = 1
class InteriorSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    Interior_poster = CommentaireSerializer(many=True, required=False)
    class Meta:
        model = Interior
        fields = '__all__'
        depth = 1
class PiscineSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    piscine =  MaisonSerializer(read_only=True ,many=True)
    class Meta:
        model = Piscine
        fields = '__all__'
        depth = 1

class VuesSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    vues =  MaisonSerializer(read_only=True ,many=True)
    
    class Meta:
        model = Vues
        fields = '__all__'
        depth = 1
class SpecificationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    specification = MaisonSerializer(read_only=True ,many=True)
    
    class Meta:
        model = Specification
        fields = '__all__'
        depth = 1
        
#-----------------------------------------TEAM---------------------------------------------------#
class PersonnelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
  
    
    class Meta:
        model = Personnel
        fields = '__all__'
        depth = 1
#++++++++++++++++-----------------------------CONFIG-------------------------###
class ContactSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = Contact
        fields = '__all__'
        depth = 2
class NewsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = News
        fields = '__all__'
        depth = 2

class DevelopmentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = Development
        fields = '__all__'
        depth = 2

class AboutsSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
   
    
    class Meta:
        model = Abouts
        fields = '__all__'
        depth = 1
class HomeSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    
    class Meta:
        model = Home
        fields = '__all__'
        depth = 1
class FeaturesSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    
    class Meta:
        model = Features
        fields = '__all__'
        depth = 2

class BackgroundSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
   
    
    class Meta:
        model = Background
        fields = '__all__'
        depth = 1
class ImageSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    slide = AboutsSerializer(read_only=True ,many=True)
    
    class Meta:
        model = Image
        fields = '__all__'
        depth = 1