from django import forms
from django.forms import ModelForm
from pages.models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        exclude = ('allowed_entries',)
