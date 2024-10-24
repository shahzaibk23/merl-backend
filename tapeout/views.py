from django.shortcuts import render
from .models import Tapeout
from pages.utils import get_nav

# Create your views here.

def all_tapeouts_view(request):

    tapeouts = Tapeout.objects.all()

    context = {
        "tapeouts":tapeouts
    }

    context.update(get_nav())

    return render(request, "tapeouts.html", context)

def tapeout_details(request, tapeout_id):
    try:
        found_tapeout = Tapeout.objects.get(id=tapeout_id)
        context = {
            'tapeout': found_tapeout
        }

        context.update(get_nav())
        return render(request, 'tapeoutdetails.html', context)
    except Tapeout.DoesNotExist:
        return HttpResponse("Tapeout not found")