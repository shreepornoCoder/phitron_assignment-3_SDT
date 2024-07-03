from django import forms
from taskCategory.models import Form_Category

class Task_category(forms.ModelForm):
    class Meta:
        model = Form_Category
        fields = "__all__"