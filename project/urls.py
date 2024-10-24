from django.urls import path
from .views import *


urlpatterns = [
    path('teams/', project_teams_view, name="project_teams"),
    path('category/<str:category>/', category_view, name="project_category"),
    path('<int:proj_id>/', project_details_view, name="project_details"),
    path('', all_projects_view, name="projects")
]