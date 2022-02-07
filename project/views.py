from django.shortcuts import render
from .models import project_teams, project, category
from pages.utils import nav_data
# Create your views here.

def projects_page(request):
    objs = project_teams.objects.all()
    mentors = [o.mentors.all() for o in objs]
    team = [o.teamMembers.all() for o in objs]
    lst = []
    for i in range(len(objs)):
        lst.append((objs[i], mentors[i], team[i], i))

    context = {
        "lst":lst[::-1],
        "nav":nav_data()
    }
    return render(request, "projects.html", context)

def project_page(request, proj_id):
    obj = project.objects.get(id=proj_id)
    context = {
        "obj":obj,
        "nav":nav_data()
    }
    return render(request, "projectPage.html", context)

def research_page(request, res_id):
    obj = category.objects.get(id=res_id) 
    objs = [a for a in project.objects.all() if a.category.name == obj.name ]
    print(objs)
    context = {
        "objs":objs,
        "nav":nav_data()
    }
    return render(request, "categories.html", context)