# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class SpecificationAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'titre')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
    )


class VuesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
    )


class PiscineAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
    )


class InteriorAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
    )


class VideoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'thumb',
        'lien',
        'nom',
        'video',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'thumb',
        'lien',
        'nom',
        'video',
    )


class MaisonAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
       
        'image_principale',
        'vues',
        
        'price',
        'lieu',
        'comming',
        'solde',
        'short',
        'size',
        'Beds',
        'Baths',
        'Garage',
        'taxe_include',
      
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
       
        'comming',
        'solde',
        'taxe_include',
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        'description',
        'image_principale',
        'vues',
        
        'price',
        'lieu',
        'comming',
        'solde',
        'short',
        'size',
        'Beds',
        'Baths',
        'Garage',
        'taxe_include',
      
    )
    raw_id_fields = ('specification',)


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Specification, SpecificationAdmin)
_register(models.Vues, VuesAdmin)
_register(models.Piscine, PiscineAdmin)
_register(models.Interior, InteriorAdmin)
_register(models.Video, VideoAdmin)
_register(models.Maison, MaisonAdmin)
