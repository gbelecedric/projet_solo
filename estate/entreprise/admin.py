from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class LinkAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'facebook',
        'twitter',
        'intagrame',
        'linkedin',
        'youtube',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'facebook',
        'twitter',
        'intagrame',
        'linkedin',
        'youtube',
    )


class InfoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'contact',
        'residential',
        'homes',
        'years',
        'complains',
        'offices',
        'adrresse',
        'maps',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'contact',
        'residential',
        'homes',
        'years',
        'complains',
        'offices',
        'adrresse',
        'maps',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Link, LinkAdmin)
_register(models.Info, InfoAdmin)
