from django.core.validators import validate_email
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import *
from entreprise.models import *

from django.shortcuts import render
from entreprise.models import *
from config_estate.models import *


# Create your views here.
def blog(request):
    query = request.GET.get('cate')
    if not query:
        article = Article.objects.filter(status=True).order_by('-date_add')
        
  
    else:
            
        article = Article.objects.filter(titre__icontains=query).order_by('-date_add')
       
    if not article.exists():
        pass
    templates_name = 'pages/blog.html'
    lien = Link.objects.filter(status=True).order_by('-date_add')
    image = Background.objects.filter(status=True).order_by('-date_add')
    categorie = Categorie.objects.filter(status=True).order_by('-date_add')
    blog = News.objects.filter(status=True).order_by('-date_add')
   
        
    
    data = {
        'image':image,
    
        'blog':blog,
       'lien':lien,
       'article':article,
       'categorie':categorie,
    
        
    }
    return render(request,templates_name,data)

def details(request , id):
    lien = Link.objects.filter(status=True).order_by('-date_add')
    image = Background.objects.filter(status=True).order_by('-date_add')
    archive = Categorie.objects.filter(status=True).order_by('-date_add') 
    alltag = Tag.objects.filter(status=True)
    article = Article.objects.get(pk=id)
    tag = article.tag_name.all()
    comment = Commentaire.objects.filter(article_id = article).order_by('-date_add')
    comment7 = Commentaire.objects.filter(article_id = article).order_by('-date_add')[5::]
    le =len(comment)
    
        # ----ORM------~#
        
    query = request.GET.get('cate')
    if not query:
            
            
            
        categorie = Categorie.objects.all()
    else:
            
        categorie = Categorie.objects.filter(titre__icontains=query)
    if not categorie.exists():
        pass
            
    
    
    templates_name = 'pages/details.html'
    data = {
        'verif':len(comment7),
         'lien':lien,
         'image':image,
        'alltag':alltag,
        'archive':archive,
        'tag':tag,
        'categorie':categorie,
        'comment':comment,
        'article':article,
    }
    return render(request,templates_name,data)
def category(request ,id):
    lien = Link.objects.filter(status=True).order_by('-date_add')
    cate = Categorie.objects.get(pk=id)
    article = Article.objects.filter(categorie_id=cate)
    
    article4 = Article.objects.filter(categorie_id=cate)[3::]

    categorie = Categorie.objects.filter(status=True)
    templates_name = 'pages/category.html'
    data = {
        'lien':lien,
    
        'categorie':categorie,
        'cate':cate ,
        'article':article,
        'verif':len(article4),
    }
    return render(request,templates_name,data)


@csrf_exempt
def senduserimage(request , id):
    print(id)
    # postdata = json.loads(request.body.decode('utf-8'))
    isemail=False
   
    img = request.FILES.get('file')
    username = request.POST.get('username')
    message = request.POST.get('message')
    email = request.POST.get('email')
    website = request.POST.get('website')
    article = Article.objects.get(pk=id)
    print(article)
    print("nom ++++++++++++++++++++",message)
    
    print("img +++++++++++++++++++",img)
    print("website +++++++++++++++++++",website)
   
    print("contenu +++++++++++++++++++",message)
    print("email +++++++++++++++++++",email)
    if ((username is not None) and (website is not None) and (message is not None) and (img is not None) and (email is not None)):
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
                myimg = Commentaire(username=username, image=img,   contenu=message,  email=email, website=website, article_id=article)
                myimg.save()
                data={
                    'success':True,
                    'message':'Vous avez commenter l\'article : {}'.format(article.titre)
                }
            except Exception as err:
                print(err)
                data={
                    'success':False,
                    'message':'Error lor de l\'enregistrement '
                }
    else:
        data={
            'success':False,
            'message':'Tous Les champs sont requis *',
        }

   
    return JsonResponse(data, safe=False)