"""icontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        re_path(r'^$', RedirectView.as_view(url='iform/list')),
        re_path(r'^tag/', include(('app.tag.urls', 'tag'), namespace='tag')),
        re_path(r'^iform/', include(('app.iform.urls','iform'), namespace='iform')),
        re_path(r'^inspection/', include(('app.inspection.urls','inspection'), namespace='inspection')),
        re_path(r'^chart/', include(('app.chart.urls', 'chart'), namespace='chart')),
        re_path(r'^admin/', admin.site.urls),
        re_path(r'^accounts/', include('django.contrib.auth.urls')),


] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
