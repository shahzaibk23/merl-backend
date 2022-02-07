from django.db import models
from django.urls import reverse
from django_mysql.models import ListCharField


from team.models import employee, mentors

# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

    def getURL(self):
        return reverse("research", kwargs={"res_id":self.id})

class project(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(category, null=True, blank=True, on_delete=models.CASCADE)
    content = models.TextField()
    thumbnail = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def getURL(self):
        return reverse("project", kwargs={"proj_id":self.id})

class project_teams(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    teamMembers = models.ManyToManyField(employee, null=True, blank=True)
    mentors = models.ManyToManyField(mentors)
    project = models.OneToOneField(project, blank=True, null=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True, blank=True)
    extra_members = ListCharField(
                base_field=models.CharField(max_length=500),
                max_length=10000,
                null=True,
                blank=True
            )

    def __str__(self):
        return self.title

    def getURL(self):
        return reverse("project", kwargs={"proj_id":self.project.id})