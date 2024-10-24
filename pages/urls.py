from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', homepage, name="home"),
    path('about/', aboutus_view, name="aboutus"),
    path('technical-advisory-board', tab_view, name="tab"),
    path('chip-launch/', chip_launch, name="chiplaunch"),
    path('dr-zahir/', dr_zahir, name="drzahir"),
    path('careers/', careers_page, name='careers'),
    path('extra/', extra_page)
]
