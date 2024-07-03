from django import forms
from task.models import Task_model

class Task_form(forms.ModelForm):
    class Meta:
        model = Task_model
        fields = '__all__'

        labels = {
            "task_title":"Task Title",
            "task_description":"Task Description",
            "task_date":"Target date",
            "is_completed":"Is Completed?",
        }

        widgets = {
            "task_title":forms.Textarea(attrs={"placeholder":"Enter The Task Title", "rows":1}),
            "task_description":forms.Textarea(attrs={"placeholder":"Enter Task Description"}),
            "task_date":forms.DateInput(attrs={"type":"date"}),
        }