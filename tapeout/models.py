from django.db import models
from project.models import Project

# Create your models here.
class Tapeout(models.Model):
    title = models.CharField(max_length=100)
    gds   = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    diagram = models.ImageField(null=True, blank=True)
    efabless_link = models.URLField(max_length = 200, blank=True, null=True)
    github_link  = models.URLField(max_length = 200, blank=True, null=True)
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE)
    mpw = models.IntegerField(null=True, blank=True)

