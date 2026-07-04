from django.urls import re_path

from app.chart.views import ChartShow

urlpatterns = (
    re_path(r'^show$', ChartShow.as_view(), name='chart_show'),
    

)
