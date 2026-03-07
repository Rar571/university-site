
from django.urls import path

from university_app.views import index, StudentListView, TeacherListView, SpecializationListView

urlpatterns = [
    path("", index, name="index"),
    path("students/", StudentListView.as_view(), name="students-list"),
    path("teachers/", TeacherListView.as_view(), name="teachers-list"),
    path("specializations/", SpecializationListView.as_view(), name="specializations-list")
]

app_name = "university_app"