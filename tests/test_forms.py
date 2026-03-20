from django.test import TestCase

from university_app.forms import (
    StudentCreationForm,
    TeacherForm,
    StudentUpdateForm,
    StudentSearchForm,
    TeacherSearchForm,
    SpecializationSearchForm,
)

from university_app.models import (
    Student,
    Teacher,
    Subject,
    Faculty,
    Specialization,
    Group
)

class FormTests(TestCase):
    def setUp(self):
        self.faculty = Faculty.objects.create(name="test_faculty", study_time=5)
        self.specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        self.group = Group.objects.create(name="test1", amount_of_students=87)
        self.subject = Subject.objects.create(name="test_subject")

    def test_student_creation_form_valid(self):
        form_data = {
            "username": "test_student",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "first_name": "John",
            "last_name": "Doe",
            "faculty": self.faculty.id,
            "specialization": self.specialization.id,
            "form_of_study": "full-time",
            "current_rating": 95,
            "group": self.group.id,
        }
        form = StudentCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_student_update_form(self):
        form_data = {
            "first_name": "John",
            "last_name": "Doe",
            "faculty": self.faculty.id,
            "specialization": self.specialization.id,
            "form_of_study": "full-time",
            "current_rating": 90,
            "group": self.group.id,
        }
        form = StudentUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_teacher_form_valid(self):
        form_data = {
            "name": "test",
            "surname": "test1",
            "specialization": self.specialization.id,
            "subjects": [self.subject.id],
            "work_experience": 3,
        }
        form = TeacherForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_student_search_form_valid(self):
        form_data = {
            "id": "1"
        }
        form = StudentSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_teacher_search_form_valid(self):
        form_data = {
            "id": "1"
        }
        form = TeacherSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_specialization_search_form_valid(self):
        form_data = {
            "name": "test_name"
        }
        form = SpecializationSearchForm(data=form_data)
        self.assertTrue(form.is_valid())




