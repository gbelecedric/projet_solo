# Generated by Django 2.2.6 on 2019-10-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('contact', models.IntegerField()),
                ('residential', models.IntegerField()),
                ('homes', models.IntegerField()),
                ('years', models.IntegerField()),
                ('complains', models.IntegerField()),
                ('offices', models.IntegerField()),
                ('adrresse', models.CharField(max_length=250)),
                ('maps', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('facebook', models.URLField()),
                ('twitter', models.URLField()),
                ('intagrame', models.URLField()),
                ('linkedin', models.URLField()),
                ('youtube', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
