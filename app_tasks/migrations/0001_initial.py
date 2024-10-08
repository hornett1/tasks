# Generated by Django 5.1 on 2024-08-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('describe', models.TextField(max_length=600)),
                ('status', models.CharField(choices=[('in_progress', 'В процесі'), ('completed', 'Виконано'), ('deferred', 'Відкладено')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('task', models.ManyToManyField(related_name='user', to='app_tasks.task')),
            ],
        ),
    ]
