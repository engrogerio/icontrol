"""icontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
        url(r'^$', RedirectView.as_view(url='iform/list')),
        url(r'^tag/', include(('app.tag.urls', 'tag'), namespace='tag')),
        url(r'^iform/', include(('app.iform.urls', 'iform'), namespace='iform')),
        url(r'^inspection/', include(('app.inspection.urls', 'inspection'), namespace='inspection')),
        url(r'^chart/', include(('app.chart.urls', 'chart'), namespace='chart')),
        url(r'^admin/', admin.site.urls),
        url(r'^accounts/', include('django.contrib.auth.urls')),
]