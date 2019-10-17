from rest_framework import viewsets, filters
from drf_dynamic_fields import DynamicFieldsMixin
from rest_framework import serializers
from entreprise.models import * 
from config_estate.models import * 
from contact.models import * 
from blog.models import * 
from house.models import * 
from team.models import * 
from .serializers import *
from drf_dynamic_fields import DynamicFieldsMixin

class CommentaireViewSet(viewsets.ModelViewSet):
       # filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.filter(status=True)
    serializer_class =  CommentaireSerializer
    
class ArticleViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Article.objects.filter(status=True)
    serializer_class =  ArticleSerializer
    
class CategorieViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Categorie.objects.filter(status=True)
    serializer_class =  CategorieSerializer
    
class TagViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Tag.objects.filter(status=True)
    serializer_class =  TagSerializer
    
    
class MessageViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Message.objects.filter(status=True)
    serializer_class =  MessageSerializer
    
class NewsletterViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Newsletter.objects.filter(status=True)
    serializer_class =  NewsletterSerializer
class LinkViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Link.objects.filter(status=True)
    serializer_class =  LinkSerializer
    
class InfoViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Info.objects.filter(status=True)
    serializer_class =  InfoSerializer
    



##==============================================================================#
    
class SpecificationViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Specification.objects.filter(status=True)
    serializer_class =  SpecificationSerializer
    
class VuesViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Vues.objects.filter(status=True)
    serializer_class =  VuesSerializer
    
class PiscineViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Piscine.objects.filter(status=True)
    serializer_class =  PiscineSerializer
    
    
class InteriorViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Interior.objects.filter(status=True)
    serializer_class =  InteriorSerializer
    
class VideoViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Video.objects.filter(status=True)
    serializer_class =  VideoSerializer
class MaisonViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Maison.objects.filter(status=True)
    serializer_class =  MaisonSerializer
class PersonnelViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Personnel.objects.filter(status=True)
    serializer_class =  PersonnelSerializer
    
#---------------------------config-----------------------#
class ContactViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Contact.objects.filter(status=True)
    serializer_class =  ContactSerializer
class NewsViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = News.objects.filter(status=True)
    serializer_class =  NewsSerializer
    
class DevelopmentViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Development.objects.filter(status=True)
    serializer_class =  DevelopmentSerializer
    
class AboutsViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Abouts.objects.filter(status=True)
    serializer_class =  AboutsSerializer
    
    
class HomeViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Home.objects.filter(status=True)
    serializer_class =  HomeSerializer
    
class FeaturesViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Features.objects.filter(status=True)
    serializer_class =  FeaturesSerializer
class BackgroundViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Background.objects.filter(status=True)
    serializer_class =  BackgroundSerializer
class ImageViewSet(viewsets.ModelViewSet):
    
       # filter_backends = (DynamicSearchFilter,)
    queryset = Image.objects.filter(status=True)
    serializer_class =  ImageSerializer
    
