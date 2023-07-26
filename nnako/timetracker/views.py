from rest_framework import generics
from .models import Member, Project, Task, Subtask
from .serializers import MemberSerializer, ProjectSerializer, TaskSerializer, SubtaskSerializer
from django.shortcuts import render

def home(request):
    content = {

    }
    return render(request, 'timetracker/home.html', content)

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubtaskListCreateView(generics.ListCreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
