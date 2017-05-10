from django.conf.urls import url

from apps.iform.views import IFormCreate, IFormList, IFormUpdate, IFormDelete

urlpatterns = [
    url(r'^create$', IFormCreate.as_view(), name='iform_create'),
    url(r'^list$', IFormList.as_view(), name='iform_list'),
    url(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', IFormUpdate.as_view(), name='iform_update'),
    url(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', IFormDelete.as_view(), name='iform_delete'),

]
