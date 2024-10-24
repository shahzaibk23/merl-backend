from django.db import models

# Create your models here.
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField()
    date = models.DateField()
    cover = models.ImageField(null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    # def getURL(self):
    #     return reverse("news2", kwargs={"news_id":self.id})