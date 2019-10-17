from django.shortcuts import render
from entreprise.models import *
from config_estate.models import *
from .models import *
# Create your views here.
def about(request):
    team = Personnel.objects.filter(status=True).order_by('-date_add')
    lien = Link.objects.filter(status=True).order_by('-date_add')
    image = Background.objects.filter(status=True).order_by('-date_add')
    about = Abouts.objects.filter(status=True).order_by('-date_add')
    
    
    info = Info.objects.filter(status=True).order_by('-date_add')
    templates_name = 'pages/about.html'
    data = {
        'info':info,
    
        'lien':lien,
         'about':about,
         'image':image, 
         'team':team,
    }
    return render(request,templates_name,data)