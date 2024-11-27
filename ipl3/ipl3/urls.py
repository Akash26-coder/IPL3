"""
URL configuration for ipl3 project.

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
import csk,rcb
from mi.views import *
from gt.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('csk/',include('csk.urls')),
    path('rcb/',include('rcb.urls')),
    path('captain/',captain,name='captain'),
    path('vicecaptain/',vicecaptain,name='vicecaptain'),
    path('captain1/',captain1,name='captain1'),
    path('vicecaptain1/',vicecaptain1,name='vicecaptain1'),
]
