from django.conf.urls import *
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='home'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.task_edit, name='task_edit'),
    # url(r'^api/tags/get/$', views.TagList.as_view()),
    url(r'^api/tags/get/', views.TagList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)