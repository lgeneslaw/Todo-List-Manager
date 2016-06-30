from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^day/(?P<year>\d{4})[-/](?P<month>\d{1,2})[-/](?P<day>\d{1,2})/$', views.day, name='day'),
    url(r'^day/$', views.day, name='day'),
    url(r'^day/(?P<year>\d{4})[-/](?P<month>\d{1,2})[-/](?P<day>\d{1,2})/completed/$', views.completed_day, name='completed_day'),
    url(r'^day/completed/$', views.completed_day, name='completed_day'),
    url(r'^week/(?P<year>\d{4})[-/](?P<month>\d{1,2})[-/](?P<day>\d{1,2})/$', views.week, name='week'),
    url(r'^week/$', views.week, name='week'),
    url(r'^task/edit/(?P<pk>\d+)/$', views.edit_task, name='edit_task'),
    url(r'^task/edit/$', views.edit_task, name='edit_task'),
    url(r'^task/delete/(?P<pk>\d+)/$', views.delete_task, name='delete_task'),
    url(r'^task/complete/(?P<pk>\d+)/$', views.complete_task, name='complete_task'),
]
