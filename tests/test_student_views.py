from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from university_app.models import Teacher, Specialization, Faculty, Subject, Group, Student

STUDENT_URL = reverse("university_app:students-list")
STUDENT_CREATE_URL = reverse("university_app:student-create")

class PublicStudentTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(STUDENT_URL)
        self.assertEqual(res.status_code, 302)


class PrivateStudentTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)
        self.faculty = Faculty.objects.create(
            name="test_faculty",
            study_time=3
        )
        self.specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        self.group = Group.objects.create(
            name="test_group",
            amount_of_students=8
        )

    def test_retrieve_student(self):
        Student.objects.create_user(
            username="username1",
            password="test1234",
            faculty=self.faculty,
            specialization=self.specialization,
            form_of_study="test_study",
            current_rating=98,
            group=self.group
        )
        response = self.client.get(STUDENT_URL)
        self.assertEqual(response.status_code, 200)
        students = Student.objects.all()
        self.assertEqual(list(response.context["student_list"]), list(students))
        self.assertTemplateUsed(response, "university_app/student_list.html")

    def test_search_student_by_id(self):
        student = Student.objects.create_user(
            username="username1",
            password="test1234",
            faculty=self.faculty,
            specialization=self.specialization,
            form_of_study="test_study",
            current_rating=98,
            group=self.group
        )
        response = self.client.get(STUDENT_URL, {"id": student.id})
        self.assertEqual(len(response.context["student_list"]), 1)

    def test_student_detail(self):
        student = Student.objects.create_user(
            username="username1",
            password="test1234",
            faculty=self.faculty,
            specialization=self.specialization,
            form_of_study="test_study",
            current_rating=98,
            group=self.group
        )
        url = reverse("university_app:student-detail", args=[student.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["student"], student)

    def test_create_student_page(self):
        response = self.client.get(STUDENT_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        form = {
            "username": "test1",
            "password1": "StrongTestPassword123!",
            "password2": "StrongTestPassword123!",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "faculty": self.faculty.id,
            "specialization": self.specialization.id,
            "form_of_study": "test_study",
            "current_rating": 98,
            "group": self.group.id
        }
        response = self.client.post(STUDENT_CREATE_URL, form)
        self.assertEqual(response.status_code, 302)
        student = Student.objects.get(username="test1")
        self.assertTrue(Student.objects.filter(username="test1").exists())

    def test_student_update(self):
        student = Student.objects.create_user(
            username="username1",
            password="test1234",
            faculty=self.faculty,
            specialization=self.specialization,
            form_of_study="test_study",
            current_rating=98,
            group=self.group
        )
        url = reverse("university_app:student-update", args=[student.id])
        form = {
            "username": "test1",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "faculty": self.faculty.id,
            "specialization": self.specialization.id,
            "form_of_study": "test_study",
            "current_rating": 98,
            "group": self.group.id
        }
        response = self.client.post(url, form)
        self.assertEqual(response.status_code, 302)
        student.refresh_from_db()
        self.assertEqual(student.first_name, "test_first_name")

    def test_student_delete(self):
        student = Student.objects.create_user(
            username="username1",
            password="test1234",
            faculty=self.faculty,
            specialization=self.specialization,
            form_of_study="test_study",
            current_rating=98,
            group=self.group
        )
        url = reverse("university_app:student-delete", args=[student.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Student.objects.filter(id=student.id).exists())

