from django.shortcuts import render

from .models import mentors, employee, technical_board
from pages.utils import nav_data
# Create your views here.
def team_page(request):
    objs = mentors.objects.all()
    objs2 = employee.objects.all()
    researchAssociates = [obj for obj in objs2 if "Research Associate" in obj.title]
    physicalDesignEngrs = [obj for obj in objs2 if "Physical Design Engineer" in obj.title]
    researchAssistants = [obj for obj in objs2 if "Research Assistant" in obj.title and "Graduate" not in obj.title]
    graduateResearchAssistants = [obj for obj in objs2 if "Graduate Research Assistant" in obj.title]
    researchInterns = [obj for obj in objs2 if "Research Intern" in obj.title]
    interns = [obj for obj in objs2 if "Intern" in obj.title and "Research" not in obj.title]
    employees = researchAssociates + physicalDesignEngrs + researchAssistants + graduateResearchAssistants + researchInterns + interns

    context = {
        "mentors":objs,
        "employees":employees,
        "nav":nav_data()
    }
    return render(request, "team.html", context)

def emp_details_page(request, emp_id):
    obj = employee.objects.get(id=emp_id)
    context = {
        "obj":obj,
        "nav":nav_data()
    }
    return render(request, "profile.html", context)

def tech_board_page(request):
    objs = technical_board.objects.all()
    context = {
        "objs":objs,
        "nav":nav_data()
    }
    return render(request, "tab.html", context)