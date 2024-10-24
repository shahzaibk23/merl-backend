from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', team_home_view, name="teamhome"),
    path('<str:emp_name>/', team_details_view, name="teamdetails")
]
