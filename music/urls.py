# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'), # ^ = beginning, $ = end
    # /music/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), # [0-9] = from 0 to 9, + = several digits. 712 is gonna hit
]