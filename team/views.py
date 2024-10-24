from django.shortcuts import render
from .models import Mentors, Employee
from pages.utils import get_nav

# Create your views here.
def team_home_view(request):

    mentors_list = Mentors.objects.all()
    employee_list = Employee.objects.all()

    context = {
        "mentors":mentors_list,
        "employees": employee_list
    }

    context.update(get_nav())

    return render(request, "team.html", context)

def team_details_view(request, emp_name):
    # Convert the URL parameter to the original name
    original_name = emp_name.replace('-', ' ').title()

    # Find the employee object with the original name
    try:
        employee = Employee.objects.get(name__iexact=original_name)
        context = {
            'employee': employee,
            "title":f"{employee.name} | {employee.title}",
            "description": employee.description[:200],
            "card": employee.picture.url
        }

        context.update(get_nav())
        return render(request, 'portfolio.html', context)
    except Employee.DoesNotExist:
        return HttpResponse("Employee not found")
