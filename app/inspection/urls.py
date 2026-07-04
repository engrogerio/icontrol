from django.urls import re_path

from app.inspection.views import InspectionList, InspectionDelete
from app.inspection.views import inspection_create, inspection_update, get_data_collections #, inspection_data_collections
urlpatterns = [
    re_path(r'^list$', InspectionList.as_view(), name='inspection_list'),

    re_path(r'^values/(?P<iform_pk>[0-9A-Za-z-]+)/$', get_data_collections, name='inspection_values'),

    re_path(r'^delete/(?P<pk>\d+)/$', InspectionDelete.as_view(), name='inspection_delete'),

    # This pattern is passing the UUID from the iform we want to create the inspection from.
    re_path(r'^create/(?P<pk>[0-9A-Za-z-]+)/$', inspection_create, name='inspection_create'),

    # These patterns are passing the inspection ID itself.
    re_path(r'^update/(?P<pk>\d+)/$', inspection_update, name='inspection_update'),

]
