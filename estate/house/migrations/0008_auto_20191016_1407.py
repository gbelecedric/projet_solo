# Generated by Django 2.2.6 on 2019-10-16 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0007_property_maison'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='maison',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maison', to='house.Maison'),
        ),
    ]
