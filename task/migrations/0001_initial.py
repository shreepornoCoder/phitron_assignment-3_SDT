# Generated by Django 5.0.6 on 2024-07-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task_model',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_title', models.CharField(max_length=200)),
                ('task_description', models.TextField(default='')),
                ('is_completed', models.BooleanField(default=False)),
                ('task_date', models.DateField()),
            ],
        ),
    ]