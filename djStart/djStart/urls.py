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
from apps.message.views import LoginView
from apps.message.views import RegisterView
from apps.expert.views import MainView
from django.views.generic import TemplateView
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^login/$', getlogin, name='Login'),
    url(r'^login/$', LoginView.as_view(), name="Login"),
    url(r'^register/$', RegisterView.as_view(), name="Register"),
    url(r'^login2/$', TemplateView.as_view(template_name="login2.html"), name="Login2"),
    url(r'^main/$', MainView.as_view(), name="Main"),
    url(r'^captcha/', include('captcha.urls')),
]
