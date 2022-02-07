from django.contrib import admin
from .models import project_teams, project, category

# Register your models here.
admin.site.register(project_teams)
admin.site.register(project)
admin.site.register(category)