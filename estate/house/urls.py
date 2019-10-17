from . import views
from django.urls import path 
urlpatterns = [
    path('', views.home, name='home'),
    path('developments', views.developments, name='developments'),
    path('<int:id>/property', views.property, name='property'),
    

]