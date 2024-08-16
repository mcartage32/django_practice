from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html',{
        'projects': projects
    })

def task(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
        
    })

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def createProject(request):
    return render(request,'create_project.html')