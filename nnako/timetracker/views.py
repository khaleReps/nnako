from rest_framework import generics

from .models import Member, Project, Task, Subtask 
from .serializers import MemberSerializer, ProjectSerializer, TaskSerializer, SubtaskSerializer
from .forms import MemberForm, ProjectsForm, TasksForm, SubtasksForm

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views import View
from django.urls import reverse

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        form = MemberForm()
        members = self.get_queryset()
        context = {
            'form': form,
            'members': members
        }
        return render(request, 'timetracker/member_list.html', context)

    def post(self, request, *args, **kwargs):
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return success response for AJAX requests
                return JsonResponse({'success': True})
            return redirect('timetracker:member-list')  # Redirect to member list after successful creation

        # If form is invalid, render the list view with form errors
        members = self.get_queryset()
        context = {
            'form': form,
            'members': members
        }
        return render(request, 'timetracker/member_list.html', context)

class MemberRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        context = {
            'member': instance,
            'object': serializer.data
        }
        return render(request, 'timetracker/member_detail.html', context)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        form = MemberForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()  
            serializer = self.get_serializer(instance)
            return JsonResponse(serializer.data)  
        else:
            context = {
                'member': instance,
                'form': form,
            }
            return render(request, 'timetracker/member_detail.html', context)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()

        return redirect('timetracker:member-list')

# ===============================================
# =============================================== 


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    def get(self, request, *args, **kwargs):
        form = ProjectsForm()
        project = self.get_queryset()
        context = {
            'form': form,
            'projects': project
        }
        return render(request, 'timetracker/projects_list.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ProjectsForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Return success response for AJAX requests
                return JsonResponse({'success': True})
            return redirect('timetracker:project-list')  # Redirect to member list after successful creation

        # If form is invalid, render the list view with form errors
        project = self.get_queryset()
        context = {
            'form': form,
            'projects': project
        }
        return render(request, 'timetracker/projects_list.html', context)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        context = {
            'project': instance,
            'object': serializer.data
        }
        return render(request, 'timetracker/project_detail.html', context)

# ===============================================
# =============================================== 

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # template_name = 'task_list.html'


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # template_name = 'task_detail.html'


class TaskListView(View):
    def get(self, request):
        tasks = Task.objects.all()
        form = TasksForm()
        return render(request, 'timetracker/task_list.html', {'task_list': tasks, 'form': form})

class TaskDetailView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        return render(request, 'timetracker/task_detail.html', {'task': task})

class TaskCreateView(View):
    def get(self, request):
        form = TasksForm()
        return render(request, 'timetracker/task_form.html', {'form': form})

    def post(self, request):
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('timetracker:task-list'))
        return render(request, 'timetracker/task_form.html', {'form': form})

class TaskUpdateView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        form = TasksForm(instance=task)
        return render(request, 'timetracker/task_form.html', {'form': form, 'task': task})

    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect(reverse('timetracker:task-detail', args=[pk]))
        return render(request, 'timetracker/task_form.html', {'form': form, 'task': task})

class TaskDeleteView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        return render(request, 'timetracker/task_confirm_delete.html', {'task': task})

    def post(self, request, pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return redirect('timetracker:task-list')     
        # return redirect(reverse('timetracker:task-list'))

# ===============================================
# =============================================== 


class SubtaskListCreateView(generics.ListCreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

    def get(self, request, *args, **kwargs):
        form = SubtasksForm()
        subtask = self.get_queryset()
        context = {
            'form': form,
            'subtasks': subtask
        }
        return render(request, 'timetracker/subtasks_list.html', context)

class SubtaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        context = {
            'subtask': instance,
            'object': serializer.data
        }
        return render(request, 'timetracker/subtasks_detail.html', context)
    
