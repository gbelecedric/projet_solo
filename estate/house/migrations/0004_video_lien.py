# Generated by Django 2.2.6 on 2019-10-16 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0003_maison_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='lien',
            field=models.URLField(blank=True),
        ),
    ]
