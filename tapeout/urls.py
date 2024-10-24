from django.urls import path
from .views import *


urlpatterns = [
    path('', all_tapeouts_view, name="all_tapeouts"),
    path('<int:tapeout_id>/', tapeout_details, name="tapeout_details")
]