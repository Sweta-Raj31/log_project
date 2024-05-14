"""
URL configuration for log_control_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from log_ingestor.views import *

from log_ingestor import views as log_views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('log/',ReactView.as_view(),name="log"),
    #  path('log/', log_views.log_api, name='log_api'),
  path('query_interface/', log_views.query_interface, name='query_interface'),
#   path('check_logs/', check_logs, name='check_logs'),
]

