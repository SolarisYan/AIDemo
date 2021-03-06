"""APIDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include

from demo.views import login

from demo.forms.user import UserRegister

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('home.urls')),
    url(r'^demo/', include('demo.urls',)),
    url(r'^accounts/login/$', login.login, name='login'),
    url(r'^accounts/logout/$', login.logout, name='logout'),
    # url(r'^accounts/register/$', login.register, name='register'),
    url(r'^register/$', UserRegister.as_view(), name='register'),
]
