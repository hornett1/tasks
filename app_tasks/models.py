from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=30)
    describe = models.TextField(max_length=600)
    status = models.CharField(choices=[
        ("in_progress", "В процесі"), 
        ("completed", "Виконано"), 
        ("deferred", "Відкладено")
    ], max_length=30)

class User(models.Model):
    username = models.CharField(max_length=30)
    task = models.ManyToManyField(Task, related_name="user")


