from django.urls import path
from . import views
from .views import MemberListCreateView, ProjectListCreateView, TaskListCreateView, SubtaskListCreateView

app_name = 'timetracker'

urlpatterns = [
    path('', views.home, name='home'), 

    path('members/', MemberListCreateView.as_view(), name='member-list-create'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('subtasks/', SubtaskListCreateView.as_view(), name='subtask-list-create'),
]
