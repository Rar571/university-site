from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from university_app.models import Teacher, Specialization, Faculty, Subject

TEACHER_URL = reverse("university_app:teachers-list")
TEACHER_CREATE_URL = reverse("university_app:teacher-create")

class PublicTeacherTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(TEACHER_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateTeacherTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test1234"
        )
        self.client.force_login(self.user)
        self.faculty = Faculty.objects.create(name="test3", study_time=5)
        self.specialization = Specialization.objects.create(name="test1",
                                                       educational_program="test2",
                                                       faculty=self.faculty)

    def test_retrieve_teacher(self):
        subject1 = Subject.objects.create(name="test6")
        subject2 = Subject.objects.create(name="test7")
        teacher = Teacher.objects.create(
            name="test",
            surname="test_surname",
            specialization=self.specialization,
            work_experience="3 years"
        )
        teacher.subjects.set([subject1, subject2])
        response = self.client.get(TEACHER_URL)
        self.assertEqual(response.status_code, 200)
        teachers = Teacher.objects.all()
        self.assertEqual(list(response.context["teacher_list"]), list(teachers))
        self.assertTemplateUsed(response, "university_app/teacher_list.html")

    def test_search_teacher_by_id(self):
        teacher = Teacher.objects.create(
            name="test",
            surname="test_surname",
            specialization=self.specialization,
            work_experience="3 years"
        )
        response = self.client.get(TEACHER_URL, {"id": teacher.id})
        self.assertEqual(len(response.context["teacher_list"]), 1)

    def test_teacher_detail(self):
        teacher = Teacher.objects.create(
            name="test",
            surname="test_surname",
            specialization=self.specialization,
            work_experience="3 years")
        url = reverse("university_app:teacher-detail", args=[teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["teacher"], teacher)

    def test_create_teacher_page(self):
        response = self.client.get(TEACHER_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_create_teacher(self):
        subject1 = Subject.objects.create(name="math")
        subject2 = Subject.objects.create(name="physics")
        form = {
            "name": "test",
            "surname": "test_surname",
            "specialization": self.specialization.id,
            "work_experience": "3 years",
            "subjects": [subject1.id, subject2.id]
        }

        response = self.client.post(TEACHER_CREATE_URL, form)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Teacher.objects.filter(name="test", surname="test_surname").exists())

    def test_update_teacher(self):
        subject1 = Subject.objects.create(name="math")
        subject2 = Subject.objects.create(name="physics")
        teacher = Teacher.objects.create(
            name="test",
            surname="test_surname",
            specialization=self.specialization,
            work_experience="3 years")
        teacher.subjects.set([subject1.id, subject2.id])
        url = reverse("university_app:teacher-update", args=[teacher.id])

        form = {
            "name": "test1",
            "surname": "test_surname1",
            "specialization": self.specialization.id,
            "work_experience": "4 years",
            "subjects": [subject1.id, subject2.id]
        }

        self.client.post(url, form)
        teacher.refresh_from_db()
        self.assertEqual(teacher.name, "test1")

    def test_delete_teacher(self):
        teacher = Teacher.objects.create(
            name="test",
            surname="test_surname",
            specialization=self.specialization,
            work_experience="3 years")

        url = reverse("university_app:teacher-delete", args=[teacher.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Teacher.objects.filter(id=teacher.id).exists())
