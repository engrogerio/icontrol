from django.conf.urls import url

from apps.inspection.views import InspectionList, InspectionDelete
from apps.inspection.views import inspection_create, inspection_update
urlpatterns = [
    url(r'^list$', InspectionList.as_view(), name='inspection_list'),
    url(r'^delete/(?P<pk>\d+)/$', InspectionDelete.as_view(), name='inspection_delete'),

    # This pattern is passing the UUID from the iform we want to create the inspection from.
    url(r'^create/(?P<pk>[0-9A-Za-z-]+)/$', inspection_create, name='inspection_create'),

    # These patterns are passing the inspection ID itself.
    url(r'^update/(?P<pk>\d+)/$', inspection_update, name='inspection_update'),

]
