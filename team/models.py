from django.db import models
from django_mysql.models import ListCharField
from django.urls import reverse



# Create your models here.
class Mentors(models.Model):
    name = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    linkedin = models.URLField(max_length = 200, blank=True, null=True)
    github = models.URLField(max_length = 200, blank=True, null=True)
    twitter = models.URLField(max_length = 200, blank=True, null=True)
    mail = models.EmailField(max_length = 200, blank=True, null=True)
    picture = models.ImageField(blank=True,  null=True)
    
    # def __init__(self):
    #     self.name = name
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=70)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    skills = ListCharField(
                base_field=models.CharField(max_length=500),
                max_length=10000
            )
    projects = ListCharField(
                base_field=models.CharField(max_length=500),
                max_length=10000
            )
    Interest = ListCharField(
                base_field=models.CharField(max_length=500),
                max_length=10000
            )
    linkedin = models.URLField(max_length = 200, blank=True, null=True)
    github = models.URLField(max_length = 200, blank=True, null=True)
    twitter = models.URLField(max_length = 200, blank=True, null=True)
    mail = models.EmailField(max_length = 200, blank=True, null=True)
    picture = models.ImageField(blank=True,  null=True)
    period = models.CharField(null=True, blank=True, max_length=500)
    priority = models.IntegerField()

    def __str__(self):
        return self.name

    def get_details(self):
         # Convert the name to lowercase and replace spaces with dashes
        filtered_name = self.name.lower().replace(' ', '-')

        # Pass the filtered name to the reverse function
        return reverse("teamdetails", kwargs={"emp_name": filtered_name})

class Technical_board(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    linkedin = models.URLField()
    picture = models.ImageField(blank=True,  null=True)

    def __str__(self):
        return self.name