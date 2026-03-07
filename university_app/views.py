from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from university_app.models import Faculty, Specialization, Subject, Teacher, Student, Group


@login_required
def index(request: HttpRequest) -> HttpResponse:
    #View for home page
    num_faculty = Faculty.objects.count()
    num_specialization = Specialization.objects.count()
    num_subject = Subject.objects.count()
    num_teacher = Teacher.objects.count()
    num_student = Student.objects.count()
    num_group = Group.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_faculty": num_faculty,
        "num_specialization": num_specialization,
        "num_subject": num_subject,
        "num_teacher": num_teacher,
        "num_student": num_student,
        "num_group": num_group,
        "num_visits": num_visits + 1
    }
    return render(request, "university_app/index.html", context=context)


class StudentListView(LoginRequiredMixin, generic.ListView):
    model = Student


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student


class TeacherListView(LoginRequiredMixin, generic.ListView):
    model = Teacher


class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Teacher


class SpecializationListView(LoginRequiredMixin, generic.ListView):
    model = Specialization


class SpecializationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Specialization