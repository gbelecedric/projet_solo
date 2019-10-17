# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class ImageAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'image')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'image',
    )


class BackgroundAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'about',
        'properti',
        'develop',
        'contact',
        'details',
        'new',
        'category',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'about',
        'properti',
        'develop',
        'contact',
        'details',
        'new',
        'category',
    )


class FeaturesAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'secure',
        'eco',
        'parking',
        'community',
        'deal',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'secure',
        'eco',
        'parking',
        'community',
        'deal',
    )


class HomeAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'interior',
        'envi',
        'text',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'interior',
        'envi',
        'text',
    )


class AboutsAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'text',
        'join',
        'work',
        'text_slide',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'text',
        'join',
        'work',
        'text_slide',
    )
    # raw_id_fields = ('image',)


class DevelopmentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'text',
        'titre',
        'text_slide',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'text',
        'titre',
        'text_slide',
    )


class NewsAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'text')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'text',
    )


class ContactAdmin(admin.ModelAdmin):

    list_display = ('id', 'date_add', 'date_update', 'status', 'text')
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'id',
        'date_add',
        'date_update',
        'status',
        'text',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Image, ImageAdmin)
_register(models.Background, BackgroundAdmin)
_register(models.Features, FeaturesAdmin)
_register(models.Home, HomeAdmin)
_register(models.Abouts, AboutsAdmin)
_register(models.Development, DevelopmentAdmin)
_register(models.News, NewsAdmin)
_register(models.Contact, ContactAdmin)
