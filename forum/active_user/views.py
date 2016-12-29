from django.shortcuts import render
from .modes import active_User
from django.contrib.auth.models import User
from django.http import HttpResponse
def activeUser(request,code):
    code = str(code)
    if active_User.objects.filter(active_str=code).exists():
        active = active_User.objects.get(active_str=code)
        user = User.object.get(username=active.user)
        user.is_active="True"
        user.save()
        return HttpResponse("激活成功")
    else:
        return HttpResponse(code)
