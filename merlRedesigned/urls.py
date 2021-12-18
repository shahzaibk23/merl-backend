from django.contrib import admin
from django.urls import path
from pages.views import *
from team.views import *
from project.views import *
from talks.views import *
from trainings.views import *
from news.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page, name="home"),
    path("about/", about_page, name="about"),
    path("team/", team_page, name="teams"),
    path("technical-adivisory-board/", tech_board_page, name="tab"),
    path("projects/", projects_page, name="projects"),
    path("talks/", talks_page, name="talks"),
    path("newsroom/", newsroom_page, name="news"),
    path("newsroom/#<int:news_id>", newsroom_page2, name="news2"),
    path("careers/", careers_page, name="careers"),
    path("training/<int:train_id>", training_page, name="training"),
    path("team/<int:emp_id>", emp_details_page, name="team"),
    path("project/<int:proj_id>", project_page, name="project"),
    path("researches/<int:res_id>", research_page, name="research"),
    path("fellowship", under_dev_page, name="fellowship")
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT )