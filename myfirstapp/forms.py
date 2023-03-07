from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Task title", max_length=100)
    description = forms.CharField(widget=forms.Textarea, label="Task Description")

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=100)
