"""djStart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from apps.message.views import LoginView, RegisterView
from apps.expert.views import MainView, MainInfoView, MainResetView
from apps.admin.views import AdminView, ListView, DetailView
from django.views.generic import TemplateView
import xadmin
from django.views.static import serve
from djStart.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^login/$', getlogin, name='Login'),
    url(r'^login/$', LoginView.as_view(), name="Login"),
    url(r'^register/$', RegisterView.as_view(), name="Register"),
    url(r'^main/$', MainInfoView.as_view(), name="Main"),
    # url(r'^login2/$', TemplateView.as_view(template_name="login2.html"), name="Login2"),
    url(r'^main/info/$', MainView.as_view(), name="MainInfo"),
    url(r'^main/reset/$', MainResetView.as_view(), name="MainReset"),
    url(r'^admin/$', AdminView.as_view(), name='Admin'),
    url(r'^admin/list/$', ListView.as_view(), name='AdminList'),
    url(r'^admin/detail/(?P<username>.*)/$', DetailView.as_view(), name='ExpertDetail'),
    url(r'^captcha/', include('captcha.urls')),
    # url(r'^image/upload/$', MainView.as_view(), name="image_upload")
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT})
]
