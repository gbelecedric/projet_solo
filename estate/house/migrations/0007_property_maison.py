# Generated by Django 2.2.6 on 2019-10-16 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0006_property_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='maison',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='maison', to='house.Maison'),
            preserve_default=False,
        ),
    ]
