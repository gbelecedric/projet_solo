# Generated by Django 2.2.6 on 2019-10-16 14:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0008_auto_20191016_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specification',
            options={'verbose_name': 'specification', 'verbose_name_plural': 'specification'},
        ),
        migrations.AddField(
            model_name='maison',
            name='Baths',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maison',
            name='Beds',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maison',
            name='Garage',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maison',
            name='oreviews',
            field=tinymce.models.HTMLField(default=1, verbose_name='oreviviews'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maison',
            name='size',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maison',
            name='specification',
            field=models.ManyToManyField(to='house.Specification'),
        ),
        migrations.AddField(
            model_name='maison',
            name='taxe_include',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]