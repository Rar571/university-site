from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from university_app.models import Faculty, Specialization, Subject, Teacher, Student, Group


def index(request: HttpRequest) -> HttpResponse:
    #View for home page
    num_faculty = Faculty.objects.count()
    num_specialization = Specialization.objects.count()
    num_subject = Subject.objects.count()
    num_teacher = Teacher.objects.count()
    num_student = Student.objects.count()
    num_group = Group.objects.count()
    context = {
        "num_faculty": num_faculty,
        "num_specialization": num_specialization,
        "num_subject": num_subject,
        "num_teacher": num_teacher,
        "num_student": num_student,
        "num_group": num_group,
    }
    return render(request, "university_app/index.html", context=context)


class StudentListView(generic.ListView):
    model = Student