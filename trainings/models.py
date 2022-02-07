from django.db import models
from team.models import employee,mentors
from django.urls import reverse

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class training(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(category, null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    teamMembers = models.ManyToManyField(employee, null=True, blank=True)
    mentors = models.ManyToManyField(mentors, null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def getURL(self):
        return reverse("training", kwargs={"train_id":self.id})

    