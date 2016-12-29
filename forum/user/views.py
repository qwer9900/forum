from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .form import user_form
def add_user(request):
    if request.method == "GET":
        return render(request,"add_user.html")
    else:
        form = user_form(request.POST)
        password = request.POST["password"].strip()
        password1 = request.POST["password1"].strip()
        username = request.POST["username"]
        b = (password==password1 and password is not None )
        c = User.objects.filter(username="username").exists()
        if not(c) and form.is_valid() and password == password1:         
            user = User.objects.create_user(form.cleaned_data["username"],form.cleaned_data["email"],form.cleaned_data["password"],)
            user.is_active="False"
            user.save()
            return HttpResponse("seccess")
        else:
            return HttpResponse(c,username)
#            return render(request,"add_user.html",{"form":form,"b":b,"c":c})

