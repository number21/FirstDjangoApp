from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from .models import Task
# Create your views here.

def task_list(request):
    tasks = Task.objects.all()

    order_by = request.GET.get("order_by", "")

    if order_by in ("name", "customer", "date_end"):
        tasks = tasks.order_by(order_by)
        if request.GET.get("reverse", "") == "1":
            tasks = tasks.reverse()
    paginator = Paginator(tasks, 2) # Show 2 task per page
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

    if request.method == "POST":
        if request.POST.get("cancel_button") is not None:
            return HttpResponseRedirect(reverse("home"))
        elif request.POST.get("ok_button") is not None:
            pass
    else:
        return render(request, 'task_add.html', {})

def task_edit(request, taskid):
    return HttpResponse("Here will have an edit form {}, soon".format(taskid))

def task_delete(request, taskid):
    return HttpResponse("Here will have an delete task {}, soon".format(taskid))