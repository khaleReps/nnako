from django.urls import path
from .views import *

app_name = 'timetracker'

urlpatterns = [
    # Members
    path('members/', MemberListCreateView.as_view(), name='member-list'),
    path('members/create/', MemberListCreateView.as_view(), name='member-create'),
    path('members/<int:pk>/', MemberRetrieveUpdateDestroyView.as_view(), name='member-detail'),
    path('members/<int:pk>/update/', MemberRetrieveUpdateDestroyView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', MemberDeleteView.as_view(), name='member-delete'),
    
    # Projects
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/create/', ProjectListCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('projects/<int:pk>/update/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    
    # Tasks
    path('tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/list/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-retrieve-update-destroy'),

    path('tasks/<int:pk>/detail/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    
    # Subtasks
    path('subtasks/', SubtaskListCreateView.as_view(), name='subtask-list'),
    path('subtasks/create/', SubtaskListCreateView.as_view(), name='subtask-create'),
    path('subtasks/<int:pk>/', SubtaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
    path('subtasks/<int:pk>/update/', SubtaskRetrieveUpdateDestroyView.as_view(), name='subtask-update'),
    path('subtasks/<int:pk>/delete/', SubtaskDeleteView.as_view(), name='subtask-delete'),
]
