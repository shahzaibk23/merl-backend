from django.shortcuts import render
from .models import Category, Training
from pages.utils import get_nav

# Create your views here.

def category_view(request, category):
    # Convert the URL parameter to the original name
    # original_name = category.replace('-', ' ')

    # Find the employee object with the original name
    try:
        found_category = Category.objects.get(id=category)
        trainings = found_category.training_set.all()
        context = {
            'trainings': trainings,
            'category': found_category
        }
        context.update(get_nav())
        return render(request, 'trainingcategory.html', context)

    except Category.DoesNotExist:
        return HttpResponse("Training Category not found")

def all_trainings_view(request):

    trainings = Training.objects.all()

    context = {
        "trainings":trainings[::-1]
    }

    context.update(get_nav())
    return render(request, 'trainingall.html', context)


def training_view(request, training):
    try:
        found_training = Training.objects.get(id=training)
        context = {
            'training': found_training,
        }
        context.update(get_nav())
        return render(request, 'training.html', context)

    except Training.DoesNotExist:
        return HttpResponse("Training  not found")