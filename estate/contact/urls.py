from . import views
from django.urls import path 
urlpatterns = [

    path('contact', views.contact, name='contact'),
    path('postmessage', views.postmessage, name='postmessage'),
    path('postemail', views.postemail, name='postemail'),
     

]