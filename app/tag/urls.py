from django.urls import path, re_path, include

from app.tag.views import TagCreate, TagList, TagUpdate, TagDelete

urlpatterns = (
    re_path(r'^create$', TagCreate.as_view(), name='tag_create'),
    re_path(r'^list$', TagList.as_view(), name='tag_list'),
    re_path(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', TagUpdate.as_view(), name='tag_update'),
    re_path(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', TagDelete.as_view(), name='tag_delete'),

)
