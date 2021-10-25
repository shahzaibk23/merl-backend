# Generated by Django 3.2.8 on 2021-10-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0002_auto_20211018_0715'),
    ]

    operations = [
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('mentors', models.ManyToManyField(blank=True, null=True, to='team.mentors')),
                ('teamMembers', models.ManyToManyField(blank=True, null=True, to='team.employee')),
            ],
        ),
    ]
