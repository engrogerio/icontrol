from django.conf.urls import url

from app.chart.views import ChartShow

urlpatterns = (
    url(r'^show$', ChartShow.as_view(), name='chart_show'),
    

)
