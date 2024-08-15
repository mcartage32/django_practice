from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Task

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def about(request):
    return HttpResponse("About")

def hello(request, username):
    return HttpResponse("Hello %s" % username)

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def task(request, id):
    task = get_object_or_404(Task, id = id)
    return HttpResponse("task %s" %task.title)