from os import name

from django.urls import path

from university_app.views import (
    index,
    StudentListView,
    TeacherListView,
    SpecializationListView,
    StudentDetailView,
    TeacherDetailView,
    SpecializationDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("students/", StudentListView.as_view(), name="students-list"),
    path("teachers/", TeacherListView.as_view(), name="teachers-list"),
    path("specializations/", SpecializationListView.as_view(), name="specializations-list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher-detail"),
    path("specializations/<int:pk>/", SpecializationDetailView.as_view(), name="specialization-detail"),
]

app_name = "university_app"