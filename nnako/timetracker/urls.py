from django.urls import path
from . import views
from .views import (
    MemberListCreateView, MemberRetrieveUpdateDestroyView,
    ProjectListCreateView, ProjectRetrieveUpdateDestroyView,
    TaskListCreateView, TaskRetrieveUpdateDestroyView,
    SubtaskListCreateView, SubtaskRetrieveUpdateDestroyView,
)
app_name = 'timetracker'

urlpatterns = [
    path('members/', MemberListCreateView.as_view(), name='member-list'),
    path('members/create/', MemberListCreateView.as_view(), name='member-create'),
    path('members/<int:pk>/', MemberRetrieveUpdateDestroyView.as_view(), name='member-detail'),
    path('members/<int:pk>/update/', MemberRetrieveUpdateDestroyView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', MemberRetrieveUpdateDestroyView.as_view(), name='member-delete'),  
    
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    
    path('subtasks/', SubtaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubtaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),

]