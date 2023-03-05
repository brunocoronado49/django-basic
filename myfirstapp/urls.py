from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('projects/', views.projects),
    path('tasks/', views.tasks),

    path('hello/<str:username>', views.hello_world), # Ruta con parametros
    path('id/<int:id>', views.number_id),
]
