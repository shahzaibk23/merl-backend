from django.shortcuts import render
from .models import News
from pages.utils import get_nav


# Create your views here.
def all_new_view(request):

    all_news = News.objects.all()

    context = {
        "news" : all_news
    }

    context.update(get_nav())

    return render(request, "newsroom.html", context)