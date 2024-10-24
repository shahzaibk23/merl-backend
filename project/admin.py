from django.contrib import admin

# Register your models here.
from .models import Project_Teams, Project, Category, Eda

# Register your models here.
admin.site.register(Project_Teams)
admin.site.register(Project)
admin.site.register(Category)
admin.site.register(Eda)