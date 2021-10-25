# Generated by Django 3.2.8 on 2021-10-18 07:11

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('skills', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=1000, size=None)),
                ('projects', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=1000, size=None)),
                ('Interest', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=1000, size=None)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mentors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('mail', models.EmailField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
