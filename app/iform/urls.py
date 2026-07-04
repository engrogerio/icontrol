from django.urls import re_path

from app.iform.views import IFormList, iform_update, IFormDelete, iform_create

urlpatterns = [
    re_path(r'^create$', iform_create, name='iform_create'),
    re_path(r'^list$', IFormList.as_view(), name='iform_list'),
    re_path(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', iform_update, name='iform_update'),
    re_path(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', IFormDelete.as_view(), name='iform_delete'),

]
