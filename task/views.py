from django.shortcuts import render, redirect
from task.forms import Task_form
from . import models 
from . import forms

# Create your views here.
def add_task(request):
    if request.method == "POST":
        form = Task_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = Task_form()
    return render(request, 'add_task.html', {"forms":form})

def edit_post(request, id):
    post = models.Task_model.objects.get(pk=id)
    post_form = forms.Task_form(instance=post)

    if request.method == 'POST':
        post_form = forms.Task_form(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('showTask')
    
    return render(request, 'add_task.html', {'forms':post_form})

def delete(request, id):
    post = models.Task_model.objects.get(pk=id)
    post.delete()
    return redirect('showTask')