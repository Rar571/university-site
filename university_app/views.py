from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from university_app.forms import StudentCreationForm, TeacherForm, StudentUpdateForm, StudentSearchForm, TeacherSearchForm, SpecializationSearchForm
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

    paginate_by = 8
    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context["search_form"] = StudentSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        id = self.request.GET.get("id", "")
        if id:
            return qs.filter(id__icontains=id)
        return qs


class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student


class StudentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Student
    form_class = StudentCreationForm
    success_url = reverse_lazy("university_app:students-list")


class StudentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy("university_app:students-list")


class StudentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Student
    success_url = reverse_lazy("university_app:students-list")


class TeacherListView(LoginRequiredMixin, generic.ListView):
    model = Teacher
    paginate_by = 8

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context["search_form"] = TeacherSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        id = self.request.GET.get("id", "")
        if id:
            return qs.filter(id__icontains=id)
        return qs

class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    model = Teacher


class TeacherCreateView(LoginRequiredMixin, generic.CreateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy("university_app:teachers-list")


class TeacherUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy("university_app:teachers-list")


class TeacherDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Teacher
    success_url = reverse_lazy("university_app:teachers-list")



class SpecializationListView(LoginRequiredMixin, generic.ListView):
    model = Specialization
    paginate_by = 8

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(SpecializationListView, self).get_context_data(**kwargs)
        context["search_form"] = SpecializationSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get("name", "")
        if name:
            return qs.filter(name__icontains=name)
        return qs


class SpecializationDetailView(LoginRequiredMixin, generic.DetailView):
    model = Specialization


class SpecializationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Specialization
    fields = "__all__"
    success_url = reverse_lazy("university_app:specializations-list")


class SpecializationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Specialization
    fields = "__all__"
    success_url = reverse_lazy("university_app:specializations-list")


class SpecializationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Specialization
    success_url = reverse_lazy("university_app:specializations-list")


def register_view(request: HttpRequest) -> HttpResponse:
    return render(request, "registration/register.html")


def login_view(request: HttpRequest) -> HttpResponse:
    return render(request, "registration/login.html")