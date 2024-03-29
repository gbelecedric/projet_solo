# Generated by Django 2.2.6 on 2019-10-16 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Background',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('about', models.ImageField(upload_to='abouts')),
                ('properti', models.ImageField(upload_to='property')),
                ('develop', models.ImageField(upload_to='develop')),
                ('contact', models.ImageField(upload_to='contact')),
                ('details', models.ImageField(upload_to='details')),
                ('new', models.ImageField(upload_to='new')),
                ('category', models.ImageField(upload_to='category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=250, verbose_name='text du background')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('about', models.TextField()),
                ('properti', models.TextField()),
                ('develop', models.TextField()),
                ('contact', models.TextField()),
                ('new', models.TextField()),
                ('category', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Development',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=250, verbose_name='text du background')),
                ('titre', models.TextField(verbose_name='titre subscribe')),
                ('text_slide', models.CharField(max_length=250, verbose_name='text de subscribe')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('secure', models.CharField(max_length=250, verbose_name='secure area')),
                ('eco', models.CharField(max_length=250, verbose_name='eco-friendly homes')),
                ('parking', models.CharField(max_length=250, verbose_name='free parking')),
                ('community', models.CharField(max_length=250, verbose_name='comunity pool ')),
                ('deal', models.CharField(max_length=250, verbose_name='best deals')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('interior', models.TextField(verbose_name='interior')),
                ('envi', models.TextField(verbose_name='enviorment friendly')),
                ('text', models.CharField(max_length=250, verbose_name='text de contact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=250, verbose_name='text du background')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Abouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('text', models.CharField(max_length=250, verbose_name='text du background')),
                ('join', models.TextField(verbose_name='JOIN OUR TEAM')),
                ('work', models.TextField(verbose_name='WORK REMOTE')),
                ('text_slide', models.CharField(max_length=250, verbose_name='text de contact')),
                ('image', models.ManyToManyField(to='config_estate.Image', verbose_name='slide')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
