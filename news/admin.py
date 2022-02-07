from django.contrib import admin
from .models import category, news

# Register your models here.
admin.site.register(news)
admin.site.register(category)