# Generated by Django 3.2 on 2022-01-23 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_alter_mentors_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentors',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
