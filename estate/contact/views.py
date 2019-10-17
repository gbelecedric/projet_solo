from django.shortcuts import render
from entreprise.models import *
from config_estate.models import *
from django.core.validators import validate_email
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def contact(request):
    lien = Link.objects.filter(status=True).order_by('-date_add')
    image = Background.objects.filter(status=True).order_by('-date_add')
    about = Contact.objects.filter(status=True).order_by('-date_add')
    info = Info.objects.filter(status=True).order_by('-date_add')
    templates_name = 'pages/contact.html'
    data = {
        'info':info,
    
        'lien':lien,
        'image':image,
        'about':about,
    }
    return render(request,templates_name,data)

@csrf_exempt
def postmessage(request):
    
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 10000000:
        compt+=1
    name=postdata['name']
    email=postdata['email']
    message=postdata['message']
  
    
    print("name ++++++++++++++++++++",name)
    isemail=False
    print("name +++++++++++++++++++",email)
    print("message +++++++++++++++++++",message)
    if ((name is not None) and  (message is not None) and  (email is not None)):
        
        
        try:
            validate_email(email)
            isemail=True
        except:
            data={
                'success':False,
                'message':'Entrez un Email Valide...'
            }
        if isemail:
            try:
                myimg = Message(nom=name,  message=message,  email=email,)
                myimg.save()
                data={
                    'success':True,
                    'message':'message envoyer '
                }
            except Exception as err:
                print(err)
                data={
                    'success':False,
                    'message':'Error pendant  de l\'enregistrement '
                }
    else:
            
            
        data={
        'success':False,
        'message':'Tous Les champs sont requis *',
    }

   
    return JsonResponse(data, safe=False)
  
   
   

@csrf_exempt
def postemail(request):
    
    
    postdata = json.loads(request.body.decode('utf-8'))
    
    # name = request.POST['name']
    isSuccess=False
    compt=1
    while compt < 10000000:
        compt+=1
    
    email=postdata['emailtwo']
   
  
    
    
    isemail=False
    print("name +++++++++++++++++++",email)
   
    if  (email is not None):
        

        try:
            validate_email(email)
            isemail=True
        except:
            
            data={
                'success':False,
                'message':'champs requis...'
            }
        if isemail:
            
            try:
                myimg = Newsletter(email=email,)
                myimg.save()
                data={
                    'success':True,
                    'message':'Email envoyer '
                }
            except Exception as err:
                print(err)
                data={
                    'success':False,
                    'message':'Error pendant  de l\'enregistrement '
                }
    else:
        
            
            
        data={
        'success':False,
        'message':' Champs  requis *',
    }

   
    return JsonResponse(data, safe=False)