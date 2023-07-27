from rest_framework import generics
from .models import Member, Project, Task, Subtask  # Make sure to import the Project model here
from .serializers import MemberSerializer, ProjectSerializer, TaskSerializer, SubtaskSerializer
from django.shortcuts import render, redirect
from .forms import MemberForm
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
        return render(request, 'timetracker/member_detail.html', {'member': instance})

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
    
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class SubtaskListCreateView(generics.ListCreateAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer

class SubtaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer



# def member_list(request):
#     members = Member.objects.all()
#     return render(request, 'timetracker/members_list.html', {'members': members})

# def member_detail(request, pk):
#     member = Member.objects.get(pk=pk)
#     return render(request, 'timetracker/member_detail.html', {'member': member})

# def project_list(request):
#     projects = Project.objects.all()
#     return render(request, 'timetracker/project_list.html', {'projects': projects})

# def project_detail(request, pk):
#     project = Project.objects.get(pk=pk)
#     return render(request, 'timetracker/project_detail.html', {'project': project})

# def task_list(request):
#     tasks = Task.objects.all()
#     return render(request, 'timetracker/task_list.html', {'tasks': tasks})

# def task_detail(request, pk):
#     task = Task.objects.get(pk=pk)
#     return render(request, 'timetracker/task_detail.html', {'task': task})

# def subtask_list(request):
#     subtasks = Subtask.objects.all()
#     return render(request, 'timetracker/subtask_list.html', {'subtasks': subtasks})

# def subtask_detail(request, pk):
#     subtask = Subtask.objects.get(pk=pk)
#     return render(request, 'timetracker/subtask_detail.html', {'subtask': subtask})