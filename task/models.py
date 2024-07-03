from django.db import models
from taskCategory.models import Form_Category

# Create your models here.
class Task_model(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_title = models.CharField(max_length=200)
    task_description = models.TextField(default="")
    category = models.ManyToManyField(to=Form_Category)
    is_completed = models.BooleanField(default=False)
    task_date = models.DateField()

    def __str__(self):
        return self.task_title