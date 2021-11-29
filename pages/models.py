from django.db import models

# Create your models here.
class collabs(models.Model):
    name = models.CharField(max_length=100)
    pic  = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    