from django.contrib.auth.forms import UserCreationForm
from django import forms

from university_app.models import Student, Teacher, Subject


class StudentCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Student
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "faculty",
            "specialization",
            "form_of_study",
            "current_rating",
            "group",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({
                "class": "form-control"
            })


class TeacherForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =["first_name", "last_name", "faculty", "specialization", "form_of_study", "current_rating", "group"]


class StudentSearchForm(forms.Form):
    id = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by student ID"}))


class TeacherSearchForm(forms.Form):
    id = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by teacher ID"}))


class SpecializationSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}))




