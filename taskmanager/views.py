#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.forms import ModelForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

from .models import Task

TASKS_PER_PAGE = 10


def paginate_list(request, obj_list):
    paginator = Paginator(obj_list, TASKS_PER_PAGE)  # Show 10 task per page
    page = request.GET.get('page')
    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        result = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        result = paginator.page(paginator.num_pages)

    return result


def task_list(request):
    tasks = Task.objects.all()

    order_by = request.GET.get("order_by", "")

    if order_by in ("name", "customer", "date_end"):
        tasks = tasks.order_by(order_by)
        if request.GET.get("reverse", "") == "1":
            tasks = tasks.reverse()

    tasks = paginate_list(request, tasks)
    return render(request, 'task_list.html', {"tasks": tasks})


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse_lazy('task_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.render_unmentioned_fields = True
        # add buttons
        self.helper.layout[-1] = FormActions(Submit('add_button', u'Зберегти', css_class="btn btn-primary"))


class TaskCreate(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = "task_add.html"

    def get_success_url(self):
        return "%s?status_message=Завдання успішно додано" % reverse_lazy("home")


class TaskUpdateForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        self.helper.form_action = reverse_lazy('task_edit',
            kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.render_unmentioned_fields = True
        # add buttons
        self.helper.layout[-1] = FormActions(Submit('add_button', u'Зберегти', css_class="btn btn-primary"))


class TaskUpdate(UpdateView):
    model = Task
    template_name = "task_edit.html"
    form_class = TaskUpdateForm
    def get_success_url(self):
        return "%s?status_message=Завдання успішно збережено" % reverse_lazy("home")

class TaskDelete(DeleteView):
    model = Task
    template_name = "task_confirm_delete.html"
    success_url = reverse_lazy("home")
