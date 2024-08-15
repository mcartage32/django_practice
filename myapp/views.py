from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Project, Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def task(request):
    return render(request, 'tasks.html')

def hello(request, username):
    return HttpResponse("Hello %s" % username)

