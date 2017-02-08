# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'), # ^ = beginning, $ = end
       
    # /music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'), # [0-9] = from 0 to 9, + = several digits. 712 is gonna hit

    # /music/712/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]
