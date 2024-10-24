from django.db import models
from team.models import Employee
from django_mysql.models import ListCharField

# Create your models here.
class Partners(models.Model):
    name    = models.CharField(max_length=200)
    image   = models.ImageField(null=True, blank=True) 

    def __str__(self) -> str:
        return self.name

class NineGoldenEmployees(models.Model):
    name    = models.CharField(max_length=200)
    title   = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    employee = models.OneToOneField(Employee, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.name

    def get_details(self):
         # Convert the name to lowercase and replace spaces with dashes
        filtered_name = self.name.lower().replace(' ', '-')

        # Pass the filtered name to the reverse function
        return reverse("teamdetails", kwargs={"emp_name": filtered_name})

class TechnicalAdvisoryBoard(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=1000)
    bio = models.TextField()
    linkedin = models.URLField(blank=True, null=True)
    bg = models.ImageField(blank=True, null=True)

class Testimonials(models.Model):
    name = models.CharField(max_length=500)
    title = models.CharField(max_length=500, blank=True, null=True)
    testimonial = models.TextField()
    platform = models.CharField(max_length=500)
    link = models.URLField(blank=True, null=True)
    headshot = models.ImageField(blank=True, null=True)


class Jobs(models.Model):
    title = models.CharField(max_length=1000)
    new = models.BooleanField()
    dept = models.CharField(max_length=100)
    content = ListCharField(
                base_field=models.CharField(max_length=10000),
                max_length=10000
            )
    