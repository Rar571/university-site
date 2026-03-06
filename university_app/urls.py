
from django.urls import path

from university_app.views import index, StudentListView

urlpatterns = [
    path("", index, name="index"),
    path("students/", StudentListView.as_view(), name="students-list")
]

app_name = "university_app"