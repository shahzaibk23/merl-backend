from django.shortcuts import render

from .models import news
from pages.utils import nav_data
# Create your views here


def newsroom_page(request):
    objs = news.objects.all()
    context = {
        "objs":objs[::-1],
        "nav":nav_data()
    }
    return render(request, "newsroom.html", context)

def newsroom_page2(request, news_id):
    objs = news.objects.get(id=news_id)
    context = {
        "objs":[objs],
        "nav":nav_data()
    }
    return render(request, "newsroom.html", context)
