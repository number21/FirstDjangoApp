from django.shortcuts import render
from django.http import HttpResponse

from .models import Task
# Create your views here.

def task_list(request):
    # TODO : Підключити БД
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {"tasks": tasks})

def task_add(request):
    return HttpResponse("Here will have an add form, soon")

def task_edit(request, taskid):
    return HttpResponse("Here will have an edit form {}, soon".format(taskid))

def task_delete(request, taskid):
    return HttpResponse("Here will have an delete task {}, soon".format(taskid))