from django.urls import path
from .views import *


urlpatterns = [
    path('', all_talks_view, name="all_talks"),
]