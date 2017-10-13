from django.conf.urls import url

from app.tag.views import TagCreate, TagList, TagUpdate, TagDelete

urlpatterns = (
    url(r'^create$', TagCreate.as_view(), name='tag_create'),
    url(r'^list$', TagList.as_view(), name='tag_list'),
    url(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', TagUpdate.as_view(), name='tag_update'),
    url(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', TagDelete.as_view(), name='tag_delete'),

)
