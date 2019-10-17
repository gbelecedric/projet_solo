from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PosteAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'nom')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
    )


class PersonnelAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        'descriptions',
        'photo',
        'poste',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'poste',
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        'descriptions',
        'photo',
        'poste',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Poste, PosteAdmin)
_register(models.Personnel, PersonnelAdmin)
