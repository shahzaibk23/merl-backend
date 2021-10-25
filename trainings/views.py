from django.shortcuts import render
from .models import training
from pages.utils import nav_data

# Create your views here.
def training_page(request, train_id):
    obj = training.objects.get(id=train_id)
    context = {
        "obj":obj,
        "nav":nav_data()
    }
    return render(request, "trainings.html", context)