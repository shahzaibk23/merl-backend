from django.db import models

class platform(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Create your models here.
class testimonials(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    platform = models.ForeignKey(platform, null=True, blank=True, on_delete=models.CASCADE)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.content
