from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.forms import CreateNewProject
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
    if request.method == 'GET':
        return render(request,'create_project.html',{
        'form': CreateNewProject()
    })
    else:
        Project.objects.create(name = request.POST["name"])
        return redirect('projects')