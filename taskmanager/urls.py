#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.task_list), name='home'),
    url(r'^tasks/add$', login_required(views.TaskCreate.as_view()), name='task_add'),
    url(r'^tasks/(?P<pk>[0-9]+)/edit$', login_required(views.TaskUpdate.as_view()), name='task_edit'),
    url(r'^tasks/(?P<pk>[0-9]+)/delete$', login_required(views.TaskDelete.as_view()), name='task_delete'),
    url(r'^tasks/(?P<pk>[0-9]+)/detail$', login_required(views.TaskDetail.as_view()), name='task_detail'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]