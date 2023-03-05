from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, render
from .models import Project, Task

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    #task = Task.objects.get(id=id)
    return render(request, 'tasks.html')

# Params en urls
def hello_world(request, username):
    print(username)
    return HttpResponse(f'<h1>Hello, {username}! from Django</h1>')

def number_id(request, id):
    print(type(id))
    return HttpResponse(f'<h1>Yout ID is {id}</h1>')
