from . import views
from django.urls import path 
urlpatterns = [

    path('', views.blog, name='blog'),
    path('<int:id>/details', views.details, name='details'),
    path('<int:id>/category', views.category, name='category'),
    path('postimage/<int:id>', views.senduserimage, name='postimage')
] 