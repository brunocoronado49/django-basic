from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.
def index(request):
    title = 'Welcome stanger!!'
    return render(request, 'index.html', {
        'title': title
    })

def about(request):
    username = 'Bruce'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {
        'projects': projects
    })

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST['name'])
        return redirect('projects')


# Params en urls
def hello_world(request, username):
    print(username)
    return HttpResponse(f'<h1>Hello, {username}! from Django</h1>')

def number_id(request, id):
    print(type(id))
    return HttpResponse(f'<h1>Yout ID is {id}</h1>')
 