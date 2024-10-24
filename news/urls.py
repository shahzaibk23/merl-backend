from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', all_new_view, name="all_news")
]
