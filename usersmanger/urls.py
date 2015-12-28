#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^users/profile/$', login_required(TemplateView.as_view(template_name='profile.html')), name='profile'),
]
