from django.db import models
from django.urls import reverse

class category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Create your models here.
class news(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    date = models.DateField()
    cover = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def getURL(self):
        return reverse("news2", kwargs={"news_id":self.id})