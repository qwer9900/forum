"""forum URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from user.views import add_user,avatar
from active_user.views import activeUser
import views
from comment.views import comment
from message.views import message,message_list
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/',include('article.urls')),
    url(r'^register',add_user),
    url(r'^$',views.index),
    url(r'^active/(?P<code>\w+)$',activeUser),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^comment/create/',comment),
    url(r'^message/read/(?P<msg_id>\d+)$',message),
    url(r'^message/list/',message_list),
    url(r'^usercenter/uploadavatar/',avatar),
]
