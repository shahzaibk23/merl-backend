from django.urls import path
from .views import *


urlpatterns = [
    path('category/<int:category>/', category_view, name="training_category"),
    path('<int:training>/', training_view, name="training"),
    path('', all_trainings_view, name="trainings")
]