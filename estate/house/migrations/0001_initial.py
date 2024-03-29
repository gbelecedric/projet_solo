# Generated by Django 2.2.6 on 2019-10-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image_interior')),
            ],
            options={
                'verbose_name': 'interior',
                'verbose_name_plural': 'interieur maison',
            },
        ),
        migrations.CreateModel(
            name='Piscine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image_piscine')),
            ],
            options={
                'verbose_name': 'piscine',
                'verbose_name_plural': 'piscine',
            },
        ),
        migrations.CreateModel(
            name='Vues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image_views')),
            ],
            options={
                'verbose_name': 'vues',
                'verbose_name_plural': 'vues',
            },
        ),
        migrations.CreateModel(
            name='Maison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image_principale', models.ImageField(upload_to='image')),
                ('price', models.FloatField()),
                ('lieu', models.CharField(max_length=255)),
                ('comming', models.BooleanField(default=False)),
                ('solde', models.BooleanField(default=False)),
                ('interior', models.ManyToManyField(to='house.Interior')),
                ('piscine', models.ManyToManyField(to='house.Piscine')),
                ('vues', models.ManyToManyField(to='house.Vues')),
            ],
            options={
                'verbose_name': 'maison',
                'verbose_name_plural': 'nos maisons',
            },
        ),
    ]
