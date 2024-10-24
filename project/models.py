from django.db import models
from django.urls import reverse
from django_mysql.models import ListCharField

from team.models import Employee, Mentors

class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    def getURL(self):
        name = self.name
        newname = name.replace(" ", "-")

        return reverse("project_category", kwargs={"category":newname})

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def getURL(self):
        return reverse("project_details", kwargs={"proj_id":self.id})

class Project_Teams(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    teamMembers = models.ManyToManyField(Employee, null=True, blank=True)
    mentors = models.ManyToManyField(Mentors)
    project = models.OneToOneField(Project, blank=True, null=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    gradient  = models.CharField(max_length=1000, null=True, blank=True)
    extras = ListCharField(
                base_field=models.CharField(max_length=500),
                max_length=10000,
                null=True, blank=True
            )
    colorChoices = [
        ("barbarian", "barbarian"),
        ("archer"   , "archer"   ),
        ("giant"    , "giant"    ),
        ("goblin"   , "goblin"   ),
        ("wizard"   , "wizard"   )
    ]
    colorVariant = models.CharField(
        max_length=100,
        choices=colorChoices,
        default="barbarian"
    )
    

    def __str__(self):
        return self.title

    # def getURL(self):
    #     return reverse("project", kwargs={"proj_id":self.project.id})


class Eda(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)
    image5 = models.ImageField(null=True, blank=True)
    subtitle = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title