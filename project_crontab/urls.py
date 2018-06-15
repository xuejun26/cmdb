# coding:utf-8
from django.conf.urls import patterns, include, url
from project_crontab.views import *

urlpatterns = patterns('',
                       url(r'^cronSvn/$', cronSvn, name='cronSvn'),
                       url(r'^cronSvn/add/$', addCronSvn, name='addCronSvn'),
                       url(r'^cronSvn/del/$', delCronSvn, name='delCronSvn'),
                       url(r'^cronProject/$', cronProjectList, name='cronProjectList'),
                       url(r'^cronProject/add/$', addCronProject, name='addCronProject'),
                       url(r'^cronProject/del/$', delCronProject, name='delCronProject'),
                       url(r'^cronList/$', crontabList, name='crontabList'),
                       )
