from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

from .models import Task


# Create your views here.

def task_list(request):
    tasks = Task.objects.all()

    order_by = request.GET.get("order_by", "")

    if order_by in ("name", "customer", "date_end"):
        tasks = tasks.order_by(order_by)
        if request.GET.get("reverse", "") == "1":
            tasks = tasks.reverse()
    paginator = Paginator(tasks, 2)  # Show 2 task per page
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

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    template_name = "task_add.html"
    success_url = "/"

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    template_name = "task_edit.html"
    success_url = "/"

class TaskDelete(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("home")
