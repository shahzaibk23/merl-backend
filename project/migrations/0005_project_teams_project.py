# Generated by Django 3.2.8 on 2021-10-25 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_project_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_teams',
            name='project',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.project'),
        ),
    ]
