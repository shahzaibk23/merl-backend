from django.shortcuts import render
from .models import Talks
from pages.utils import get_nav

# Create your views here.
def all_talks_view(request):
    
    all_talks = Talks.objects.all()

    context = {
        "talks":all_talks
    }

    context.update(get_nav())

    return render(request, "talks.html", context)