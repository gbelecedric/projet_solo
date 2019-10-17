from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path , re_path
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
openapi.Info(
    title="Snippets API",
    default_version='v1',
    description="Test description",
    terms_of_service="https://www.google.com/policies/terms/",
    contact=openapi.Contact(email="contact@snippets.local"),
    license=openapi.License(name="BSD License"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)



router = DefaultRouter()
router.register('article',ArticleViewSet, base_name=' article')
router.register('category', CategorieViewSet, base_name='category')
router.register('commentaire', CommentaireViewSet, base_name='commentaire')
router.register('tag', TagViewSet, base_name='tag')
router.register('message',MessageViewSet , base_name='message')
router.register('newsletter', NewsletterViewSet, base_name='newsletter')
router.register('lien', LinkViewSet , base_name='lien')
router.register('info', InfoViewSet, base_name='info')
router.register('maison', MaisonViewSet, base_name='maison')
router.register('video', VideoViewSet, base_name='video')
router.register('interior',InteriorViewSet , base_name='interior')
router.register('piscine', PiscineViewSet, base_name='piscine')
router.register('vues', VuesViewSet , base_name='vues')
router.register('image', ImageViewSet, base_name='image')
router.register('background', BackgroundViewSet, base_name='background')
router.register('features', FeaturesViewSet, base_name='features')
router.register('home', HomeViewSet, base_name='home')
router.register('abouts',AboutsViewSet , base_name='abouts')
router.register('development', DevelopmentViewSet, base_name='development')
router.register('vues', VuesViewSet , base_name='vues')
router.register('news', NewsViewSet, base_name='news')
router.register(' contact',  ContactViewSet, base_name=' contact')

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += router.urls