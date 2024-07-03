from django.shortcuts import render, redirect
from task.models import Task_model
# from task import models

def home(request):
    return render(request, 'home.html')

def show_task(request):
    data = Task_model.objects.all()
    return render(request, 'show_task.html', {'data':data})