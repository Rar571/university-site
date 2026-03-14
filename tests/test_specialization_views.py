from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from university_app.models import Faculty, Subject, Specialization

SPECIALIZATION_URL = reverse("university_app:specializations-list")
SPECIALIZATION_CREATE_URL = reverse("university_app:specialization-create")

class PublicSpecializationTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(SPECIALIZATION_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateSpecializationTest(TestCase):
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

    def test_retrieve_specialization(self):
        subject1 = Subject.objects.create(
            name="test_subject1",
        )
        subject2 = Subject.objects.create(
            name="test_subject2",
        )
        specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        specialization.subjects.set([subject1, subject2])
        response = self.client.get(SPECIALIZATION_URL)
        self.assertEqual(response.status_code, 200)
        specializations = Specialization.objects.all()
        self.assertEqual(list(response.context["specialization_list"]), list(specializations))
        self.assertTemplateUsed(response, "university_app/specialization_list.html")

    def test_search_specialization_by_id(self):
        specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        response = self.client.get(SPECIALIZATION_URL, {"name": "test_specialization"})
        self.assertEqual(len(response.context["specialization_list"]), 1)

    def test_specialization_detail(self):
        specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        url = reverse("university_app:specialization-detail", args=[specialization.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["specialization"], specialization)

    def test_create_specialization_page(self):
        response = self.client.get(SPECIALIZATION_CREATE_URL)
        self.assertEqual(response.status_code, 200)

    def test_create_specialization(self):
        subject1 = Subject.objects.create(
            name="test_subject1",
        )
        subject2 = Subject.objects.create(
            name="test_subject2",
        )
        form = {
            "name": "test",
            "educational_program": "test_program",
            "subjects": [subject1.id, subject2.id],
            "faculty": self.faculty.id
        }
        response = self.client.post(SPECIALIZATION_CREATE_URL, form)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Specialization.objects.filter(name="test", educational_program="test_program").exists())

    def test_update_specialization(self):
        subject1 = Subject.objects.create(name="test_subject")
        specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        specialization.subjects.add(subject1)
        url = reverse("university_app:specialization-update", args=[specialization.id])
        form = {
            "name": "test",
            "educational_program": "test_program",
            "faculty": self.faculty.id,
            "subjects": [subject1.id]
        }
        response = self.client.post(url, form)
        self.assertEqual(response.status_code, 302)
        specialization.refresh_from_db()
        self.assertEqual(specialization.name, "test")

    def test_delete_specialization(self):
        specialization = Specialization.objects.create(
            name="test_specialization",
            educational_program="test_program",
            faculty=self.faculty
        )
        url = reverse("university_app:specialization-delete", args=[specialization.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Specialization.objects.filter(id=specialization.id).exists())

