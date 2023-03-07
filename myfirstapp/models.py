from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

    # Retorna el nombre de los proyectos
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    done = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Store(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=60)
    description = models.CharField(max_length=60)