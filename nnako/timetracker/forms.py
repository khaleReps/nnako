from django import forms
from .models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'


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
