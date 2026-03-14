from django.contrib.auth.models import AbstractUser
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=255, unique=True)
    study_time = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Specialization(models.Model):
    name = models.CharField(max_length=255)
    educational_program = models.CharField(max_length=255)
    subjects = models.ManyToManyField("Subject", related_name="specializations_subjects")
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name="specializations_faculty")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, related_name="teachers_specialization")
    subjects = models.ManyToManyField(Subject, related_name="teachers", blank=True)
    work_experience = models.CharField(max_length=255)


class Student(AbstractUser):
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT, related_name="students_faculty", null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, related_name="students_specialization", null=True)
    form_of_study = models.CharField(max_length=255)
    current_rating = models.PositiveIntegerField(default=0)
    group = models.ForeignKey("Group", on_delete=models.PROTECT, related_name="students_group", null=True)

    class Meta:
        ordering = ["id"]

class Group(models.Model):
    name = models.CharField(max_length=255, unique=True)
    amount_of_students = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}"
