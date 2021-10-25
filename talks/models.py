from django.db import models

# Create your models here.
class talks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name