from django.shortcuts import render
from entreprise.models import *
from config_estate.models import *
from .models import *

# Create your views here.
def home(request):
    back = Maison.objects.filter(status=True).order_by('-date_add')
    design = Interior.objects.filter(status=True).order_by('-date_add')
    localisation = Video.objects.filter(status=True).order_by('-date_add')
    
    taille = len(back)
    if taille < 3:
        back = Maison.objects.all().order_by('-date_add')
    else:
        back = Maison.objects.filter(status=True).order_by('-date_add')
    contact = Info.objects.filter(status=True).order_by('-date_add')
    lien = Link.objects.filter(status=True).order_by('-date_add')
    feat = Features.objects.filter(status=True).order_by('-date_add')
    text = Home.objects.filter(status=True).order_by('-date_add')
    templates_name = 'pages/index.html'
    data = {
        
        'info':contact,
        'feat':feat,
         'text':text,
        'loca':localisation,
         'lien':lien,
        'back': back,
        'design':design,
    }
    return render(request,templates_name,data)
def property(request ,id):
    lien = Link.objects.filter(status=True).order_by('-date_add')
    image = Background.objects.filter(status=True).order_by('-date_add')
    text = Home.objects.filter(status=True).order_by('-date_add')
    contact = Info.objects.filter(status=True).order_by('-date_add')
    house = Maison.objects.get(pk=id)
    back = Maison.objects.filter(status=True,).order_by('-date_add')
    about = Abouts.objects.filter(status=True).order_by('-date_add')
    templates_name = 'pages/property.html'
    data = {
        'about':about,
    
        'lien':lien,
         'text':text,
        'back':back,
        'info':contact,
        'image':image,
        'house':house,
    }
    return render(request,templates_name,data)
def developments(request):
    back = Maison.objects.filter(status=True).order_by('-date_add')
    lien = Link.objects.filter(status=True).order_by('-date_add')
    image = Background.objects.filter(status=True).order_by('-date_add')
    about = Abouts.objects.filter(status=True).order_by('-date_add')
    dev = Development.objects.filter(status=True).order_by('-date_add')
    
    info = Info.objects.filter(status=True).order_by('-date_add')
    templates_name = 'pages/developments.html'
    data = {
        'info':info,
         'dev':dev,
        'lien':lien,
         'about':about,
         'image':image, 
    
        'house': back,
    }
    return render(request,templates_name,data)
