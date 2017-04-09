from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .form import user_form
from active_user.models import active_User
import uuid
from django.core.mail import send_mail
def add_user(request):
    if request.method == "GET":
        return render(request,"add_user.html")
    else:
        form = user_form(request.POST)
        password = request.POST["password"].strip()
        password1 = request.POST["password1"].strip()
        username = request.POST["username"]
        b = (password==password1 and password is not None )
        strUuid = str(uuid.uuid4()).replace("-","")
        c = User.objects.filter(username=username).exists()
        active_link = "http://%s/active/%s" %(request.get_host(),strUuid)
        active_email = ''' 点击<a href="%s">这里</a>激活''' %active_link
        if not(c) and form.is_valid() and password == password1:         
            user = User.objects.create_user(form.cleaned_data["username"],form.cleaned_data["email"],form.cleaned_data["password"],)
            user.is_active="False"
            user.is_staff="True"
            user.save()
            active_user=active_User(user=form.cleaned_data["username"],active_str=strUuid)
            active_user.save()
            email = form.cleaned_data["email"]
            send_mail(subject='[pyrhonme]激活邮件',
                      message='点击链接激活:%s'%active_link,
                      html_message=active_email,
                      from_email='670399751@qq.com',
                      recipient_list=[email],
                      fail_silently=False)
            return HttpResponse("seccess")
        else:
            return render(request,"add_user.html",{"form":form,"b":b,"c":c})

