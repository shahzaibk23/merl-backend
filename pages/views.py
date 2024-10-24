from django.shortcuts import render
from asgiref.sync import sync_to_async
from django.views import View
# models
from .models import Partners, NineGoldenEmployees, TechnicalAdvisoryBoard, Testimonials, Jobs
from news.models import News
from team.models import Employee
from project.models import Project_Teams, Eda
from tapeout.models import Tapeout
# others
from .utils import get_total_stars_and_repos_in_org, get_nav


# Create your views here.
def homepage(request):

    news_objs = News.objects.all()

    projectss = Project_Teams.objects.all()[::-1]
    team_proj = [proj.teamMembers.all() for proj in projectss][:5]
    mentors = [proj.mentors.all() for proj in projectss][:5]
    projects = []
    for i in range(len(team_proj)):
        projects.append((projectss[i], team_proj[i], mentors[i]))

    edas = Eda.objects.all()[::-1]
    

    tapeouts = Tapeout.objects.all()

    testimonials = Testimonials.objects.all()

    context = {
        "github_stars": 345,
        "total_repos": 130,
        "news": news_objs,
        "projects":projects[::-1][:5][::-1],
        "tapeouts":tapeouts,
        "testimonials":testimonials,
        "edas":edas
    }

    context.update(get_nav())

    return render(request, "homepage.html", context)

def aboutus_view(request):

    employees = NineGoldenEmployees.objects.all()

    context = {
        "employee": employees
    }
    context.update(get_nav())

    return render(request, "about.html", context)

def tab_view(request):

    tabs = TechnicalAdvisoryBoard.objects.all()

    context = {
        "tabs":tabs
    }
    context.update(get_nav())

    return render(request, "tab.html", context)

def chip_launch(request):

    context = {}

    context.update(get_nav())

    return render(request, "chiplaunch.html", context)

def dr_zahir(request):

    context = {}

    context.update(get_nav())

    return render(request, "drzahir.html", context)

def careers_page(request):

    jobs = Jobs.objects.all()[::-1]

    context = {
        "jobs":jobs
    }

    context.update(get_nav())

    return render(request, "careers.html", context)

def extra_page(request):

    context = {}

    context.update(get_nav())

    return render(request, "extra.html", context)


# class MyView(View):
#     async def get_total_stars_and_repos(self, org_name):
#         # Asynchronously fetch total stars and total repositories
#         total_stars, total_repos = await get_total_stars_and_repos_in_org(org_name)
#         return total_stars, total_repos

#     async def get(self, request):
#         # Asynchronously fetch total stars and total repositories
#         total_stars, total_repos = await self.get_total_stars_and_repos('merledu')

#         partners_objs = await Partners.objects.all()

#         # Render the template with the total stars in the context
#         context = {
#             'partners':partners_objs,
#             'github_stars': total_stars,
#             'total_repos':total_repos
#         }

#         return render(request, 'homepage.html', context)