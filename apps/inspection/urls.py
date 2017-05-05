from django.conf.urls import url

from apps.inspection.views import InspectionCreate, InspectionList, InspectionUpdate, InspectionDelete
from apps.inspection.views import inspection_create
urlpatterns = [
    url(r'^create/(?P<pk>[0-9A-Za-z-]+)/$', inspection_create, name='inspection_create'),
    url(r'^list$', InspectionList.as_view(), name='inspection_list'),
    url(r'^update/(?P<pk>[0-9A-Za-z-]+)/$', InspectionUpdate.as_view(), name='inspection_update'),
    url(r'^delete/(?P<pk>[0-9A-Za-z-]+)/$', InspectionDelete.as_view(), name='inspection_delete'),

]
