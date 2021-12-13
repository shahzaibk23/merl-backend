from django.shortcuts import render
from .utils import nav_data
from project.models import project_teams
from news.models import news
from testimonials.models import testimonials
from .models import collabs
# Create your views here.

def home_page(request):
    projectss = project_teams.objects.all()[::-1]
    team_proj = [proj.teamMembers.all() for proj in projectss][:3]
    mentors = [proj.mentors.all() for proj in projectss][:3]
    news_objs = news.objects.all()
    tests = testimonials.objects.all()
    projects = []
    collab = collabs.objects.all()
    for i in range(len(team_proj)):
        projects.append((projectss[i], team_proj[i], mentors[i]))
    context = {
        "projects":projects,
        "news":news_objs[::-1][:3],
        "tests":tests[::-1],
        "nav":nav_data(),
        "c":collab
        }
    return render(request, "index.html",context )

def about_page(request):
    return render(request, "about.html", {
        "nav":nav_data()})

# def tab_page(request):
#     return render(request, "tab.html", {})

# def train_page(request):
#     return render(request, "trainings.html", {
#         "nav":nav_data()})

# def talks_page(request):
#     return render(request, "talks.html", {})

# def newsroom_page(request):
#     return render(request, "newsroom.html", {
#         "nav":nav_data()})

def careers_page(request):
    return render(request, "career.html", {
        "nav":nav_data()})


