from django.db import models

# Create your models here.
class Form_Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category