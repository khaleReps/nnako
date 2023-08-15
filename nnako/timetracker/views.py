

    # def post(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return redirect('timetracker:member-list')  # Redirect to member list after successful deletion
    
    # def put(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     form = MemberForm(request.POST, instance=instance)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('timetracker:member-list')
    #     else:
    #         context = {
    #             'member': instance,
    #             'form': form,
    #         }
    #         return render(request, 'timetracker/member_detail.html', context)

    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
        
    #     # Check if the request is an AJAX call and return JSON response
    #     if request.is_ajax():
    #         return JsonResponse({'success': True})
    #     else:
    #         return redirect('timetracker:member-list')


from rest_framework import generics
from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, Project, Task, Subtask 
from .serializers import MemberSerializer, ProjectSerializer, TaskSerializer, SubtaskSerializer
from .forms import MemberForm, ProjectsForm, TasksForm, SubtasksForm
from django.http import JsonResponse

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
            form.save()
            return redirect('timetracker:member-list')
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


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get(self, request, *args, **kwargs):
        form = TasksForm()
        task = self.get_queryset()
        context = {
            'form': form,
            'tasks': task
        }
        return render(request, 'timetracker/task_list.html', context)
    

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        context = {
            'task': instance,
            'object': serializer.data
        }
        return render(request, 'timetracker/task_detail.html', context)

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
    
