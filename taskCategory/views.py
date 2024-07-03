from django.shortcuts import render, redirect
from taskCategory.forms import Task_category

# Create your views here.
def add_category(request):
    if request.method == "POST":
        form = Task_category(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = Task_category()
    return render(request, 'add_category.html', {"forms":form})