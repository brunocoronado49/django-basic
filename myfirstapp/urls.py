from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create-task', views.create_task, name='create_task'),
    path('projects/create_project', views.create_project, name='create_project'),

    path('hello/<str:username>', views.hello_world), # Ruta con parametros
    path('id/<int:id>', views.number_id),
]
