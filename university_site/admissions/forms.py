from django import forms
from .models import Applicant

class ApplicantForm(forms.ModelForm):
    COURSE_CHOICES = [
        ('Bachelor', 'Бакалавриат'),
        ('Master', 'Магистратура'),
        ('PhD', 'Докторантура'),
    ]
    SPECIALIZATION_CHOICES = [
        ('Computer Science', 'Информатика'),
        ('Physics', 'Физика'),
        ('Mathematics', 'Математика'),
    ]

    course = forms.ChoiceField(choices=COURSE_CHOICES, label='Курс')
    specialization = forms.ChoiceField(choices=SPECIALIZATION_CHOICES, label='Специальность')

    class Meta:
        model = Applicant
        fields = ['first_name', 'last_name', 'email', 'phone']


