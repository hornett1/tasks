import sys
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_tasks.settings")
django.setup()

from app_tasks.models import *

user1 = User(username="Josh")
task1 = Task(name="УП 3", describe="Django ORM", status="Виконано")

user1.save()
task1.save()

user = User.objects.get(id=1)
task = Task.objects.get(id=1)

user.task.add(task)

while True:
    print("1 - Change task status")
    a = input()
    if a == "1":
        b = input("Choose between Виконано, В процесі, Відкладено")
        task1.status = b
        print("Successfull")