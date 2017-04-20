from django.shortcuts import render,redirect
from .models import Message


def message(request,msg_id):
    msg_id=int(msg_id)
    msg = Message.objects.get(id=msg_id)
    msg.status = 0
    msg.save()
    return redirect("/article/detail/%s" % msg.link)
def message_list(request):
    msg = Message.objects.filter(owner=request.user,status=-1).order_by("-id")
    return render(request,"message.html",{"unread_messages":msg})

