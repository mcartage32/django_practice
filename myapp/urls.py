from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('about', views.about, name="about"),
    path('hello/<str:username>', views.hello, name="hello"),
    path('projects', views.projects, name="projects"),
    path('tasks', views.task, name="tasks"),
    path('create-project', views.createProject, name="create-project")
]