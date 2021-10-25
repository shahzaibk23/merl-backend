from django.shortcuts import render

from .models import mentors, employee, technical_board
from pages.utils import nav_data
# Create your views here.
def team_page(request):
    objs = mentors.objects.all()
    objs2 = employee.objects.all()
    context = {
        "mentors":objs,
        "employees":objs2,
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