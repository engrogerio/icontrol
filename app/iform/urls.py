from django.conf.urls import url

from app.iform.views import IFormList, iform_update, IFormDelete, iform_create

urlpatterns = [
    url(r'^create$', iform_create, name='iform_create'),
    url(r'^list$', IFormList.as_view(), name='iform_list'),
    url(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', iform_update, name='iform_update'),
    url(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', IFormDelete.as_view(), name='iform_delete'),

]
