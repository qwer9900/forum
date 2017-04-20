from django.shortcuts import render
from block.models import Block
from message.models import Message
def index(request):
    block_info = Block.objects.filter(status=0).order_by("-id")
    msg_cnt = 0
    if request.user.is_authenticated():
        msg_cnt = Message.objects.filter(status=-1,owner=request.user).count()
    return render(request,"index.html",{"blocks":block_info,"msg_cnt":msg_cnt})
    
