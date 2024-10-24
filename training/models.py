from django.db import models
from team.models import Employee,Mentors
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    def getURL(self):
        return reverse("training_category", kwargs={"category":self.id})

class Training(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    teamMembers = models.ManyToManyField(Employee, null=True, blank=True)
    mentors = models.ManyToManyField(Mentors, null=True, blank=True)
    thumbnail = models.ImageField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title

    def getURL(self):
        return reverse("training", kwargs={"training":self.id})

    