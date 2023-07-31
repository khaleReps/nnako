from django import forms
from .models import Member
from django.forms.widgets import DateInput, TimeInput

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ('employee_id','employment_status', 'work_hours')
        widgets = {
            'hire_date':  DateInput(attrs={'type': 'date'}),
            'date_of_birth':  DateInput(attrs={'type': 'date'}),
        }


class ProjectsForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class TasksForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


class SubtasksForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
