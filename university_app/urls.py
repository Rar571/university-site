from django.urls import path

from university_app.views import (
    index,
    StudentListView,
    TeacherListView,
    SpecializationListView,
    StudentDetailView,
    TeacherDetailView,
    SpecializationDetailView, StudentCreateView, TeacherCreateView, SpecializationCreateView, StudentUpdateView, TeacherUpdateView, SpecializationUpdateView, StudentDeleteView, SpecializationDeleteView, TeacherDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("students/", StudentListView.as_view(), name="students-list"),
    path("teachers/", TeacherListView.as_view(), name="teachers-list"),
    path("specializations/", SpecializationListView.as_view(), name="specializations-list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher-detail"),
    path("specializations/<int:pk>/", SpecializationDetailView.as_view(), name="specialization-detail"),
    path("students/create/", StudentCreateView.as_view(), name="student-create"),
    path("teachers/create/", TeacherCreateView.as_view(), name="teacher-create"),
    path("specializations/create/", SpecializationCreateView.as_view(), name="specialization-create"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("teachers/<int:pk>/update/", TeacherUpdateView.as_view(), name="teacher-update"),
    path("specializations/<int:pk>/update/", SpecializationUpdateView.as_view(), name="specialization-update"),
    path("students/<int:pk>/delete", StudentDeleteView.as_view(), name="student-delete"),
    path("teachers/<int:pk>/delete/", TeacherDeleteView.as_view(), name="teacher-delete"),
    path("specializations/<int:pk>/delete", SpecializationDeleteView.as_view(), name="specialization-delete"),

]

app_name = "university_app"