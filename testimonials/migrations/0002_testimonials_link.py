# Generated by Django 3.2.8 on 2021-10-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
