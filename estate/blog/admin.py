# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class TagAdmin(admin.ModelAdmin):

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


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
        'nom',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'nom',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'image',
        'nom',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'description',
        'categorie_id',
        'contenu',
        'photo',
        'nom',
        'nbr_comment',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'categorie_id',
        'nom',
        'id',
        'date_add',
        'date_update',
        'status',
        'titre',
        'description',
        'categorie_id',
        'contenu',
        'photo',
        'nom',
        'nbr_comment',
    )
    raw_id_fields = ('tag_name',)


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'email',
        'website',
        'contenu',
        'image',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'article_id',
        'id',
        'date_add',
        'date_update',
        'status',
        'article_id',
        'username',
        'email',
        'website',
        'contenu',
        'image',
    )


class ReplyAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        'email',
        'website',
        'comment',
        'contenu',
        'image',
    )
    list_filter = (
        'date_add',
        'date_update',
        'status',
        'comment',
        'id',
        'date_add',
        'date_update',
        'status',
        'nom',
        'email',
        'website',
        'comment',
        'contenu',
        'image',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Tag, TagAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
_register(models.Reply, ReplyAdmin)
