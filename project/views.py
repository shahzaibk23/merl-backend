from django.shortcuts import render
from .models import Project_Teams, Category, Project
from pages.utils import get_nav

# Create your views here.
def project_teams_view(request):

    teams = Project_Teams.objects.all()[::-1]

    context = {
        "teams":teams
    }

    context.update(get_nav())

    return render(request, "projteam.html", context)

def all_projects_view(request):
    projects = Project.objects.all()

    context = {
        "projects":projects[::-1]
    }
    context.update(get_nav())

    return render(request, "projall.html", context)

def project_details_view(request, proj_id):
    try:
        found_project = Project.objects.get(id = proj_id)

        context = {
            "project":found_project
        }

        context.update(get_nav())

        return render(request, "projdetails.html", context)

    except Project.DoesNotExist:
        return HttpResponse("Project not found")


def category_view(request, category):
     # Convert the URL parameter to the original name
    original_name = category.replace('-', ' ')

    # Find the employee object with the original name
    try:
        found_category = Category.objects.get(name__iexact=original_name)
        projects = found_category.project_set.all()
        context = {
            'projects': projects,
            'category': found_category
        }

        context.update(get_nav())
        return render(request, 'projcategory.html', context)
    except Category.DoesNotExist:
        return HttpResponse("Project Category not found")