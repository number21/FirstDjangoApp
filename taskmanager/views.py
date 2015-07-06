from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def task_list(request):
    # TODO : Підключити БД
    tasks = (
        {"id": 1,
         "name": "Виписати піздюлей",
         "customer": "Я",
         "status": "В процесі",
         "date_start": "21.01.2015",
         "date_end": "21.02.2015",
         "estimated_time": 30*24},
        {"id": 2,
         "name": "Вламати піздюлей",
         "customer": "Я",
         "status": "В процесі",
         "date_start": "30.06.2015",
         "date_end": "30.07.2015",
         "estimated_time": 30*24},
        {"id": 3,
         "name": "Вламати піздюлей",
         "customer": "Я",
         "status": "Виконано",
         "date_start": "30.06.2015",
         "date_end": "30.07.2015",
         "estimated_time": 30*24},
        {"id": 4,
         "name": "Вламати піздюлей",
         "customer": "Я",
         "status": "Прийнято",
         "date_start": "30.06.2015",
         "date_end": "30.07.2015",
         "estimated_time": 30*24},



    )
    return render(request, 'task_list.html', {"tasks": tasks})

def task_add(request):
    return HttpResponse("Here will have an add form, soon")

def task_edit(request, taskid):
    return HttpResponse("Here will have an edit form {}, soon".format(taskid))

def task_delete(request, taskid):
    return HttpResponse("Here will have an delete task {}, soon".format(taskid))