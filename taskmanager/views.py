from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 2) # Show 25 contacts per page
    order_by = request.GET.get("order_by", "")

    if order_by in ("name", "customer", "date_end"):
        tasks = tasks.order_by(order_by)
        if request.GET.get("reverse", "") == "1":
            tasks = tasks.reverse()

    page = request.GET.get('page')
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tasks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tasks = paginator.page(paginator.num_pages)

    return render(request, 'task_list.html', {"tasks": tasks})

def task_add(request):
    return HttpResponse("Here will have an add form, soon")

def task_edit(request, taskid):
    return HttpResponse("Here will have an edit form {}, soon".format(taskid))

def task_delete(request, taskid):
    return HttpResponse("Here will have an delete task {}, soon".format(taskid))