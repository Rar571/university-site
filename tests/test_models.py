from django.test import TestCase
from university_app.models import Faculty, Specialization, Subject, Group, Student


class ModelsTests(TestCase):
    def test_faculty_str(self):
        faculty = Faculty.objects.create(name="test", study_time=5)
        self.assertEqual(str(faculty), faculty.name)

    def test_specialization_str(self):
        faculty = Faculty.objects.create(name="test", study_time=5)
        subject1 = Subject.objects.create(name="subject1")
        subject2= Subject.objects.create(name="subject2")
        specialization = Specialization.objects.create(name="test", educational_program="test1", faculty=faculty)
        specialization.subjects.set([subject1, subject2])
        self.assertEqual(str(specialization), specialization.name)

    def test_create_student(self):
        username = "test"
        password = "test1234"
        faculty = Faculty.objects.create(name="test_faculty", study_time=5)
        specialization = Specialization.objects.create(name="test_specialization", educational_program="test_program", faculty=faculty)
        form_of_study = "test_study"
        group = Group.objects.create(name="test_group", amount_of_students=12)
        student = Student.objects.create_user(
            username=username,
            password=password,
            faculty=faculty,
            specialization=specialization,
            form_of_study=form_of_study,
            group=group,
        )
        self.assertEqual(student.username, username)
        self.assertTrue(student.check_password(password))
        self.assertEqual(student.faculty, faculty)
        self.assertEqual(student.specialization, specialization)
        self.assertEqual(student.form_of_study, form_of_study)
        self.assertEqual(student.group, group)
        self.assertEqual(student.current_rating, 0)

    def test_subject_str(self):
        subject = Subject.objects.create(name="test")
        self.assertEqual(str(subject), subject.name)

    def test_group_str(self):
        group = Group.objects.create(name="test", amount_of_students=14)
        self.assertEqual(str(group), group.name)
        




