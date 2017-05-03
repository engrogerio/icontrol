from django.conf.urls import url

from apps.iform.views import FormCreate, FormList, FormUpdate, FormDelete

urlpatterns = [
    url(r'^create$', FormCreate.as_view(), name='iform_create'),
    url(r'^list$', FormList.as_view(), name='iform_list'),
    url(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', FormUpdate.as_view(), name='iform_update'),
    url(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', FormDelete.as_view(), name='iform_delete'),

]
