from django.shortcuts import render
from .models import talks
from pages.utils import nav_data

# Create your views here.
def talks_page(request):
    objs = talks.objects.all()
    context = {
        "talks":objs,
        "nav":nav_data()
    }
    return render(request, "talks.html", context)


    # nthere is no white chips, either it is grey or black -- naveed sherwani