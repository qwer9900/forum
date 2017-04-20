from django.shortcuts import render
from .models import Comment
from pyTojs import json_response
def comment(request):
    if request.method == "POST":
        com = request.POST["parm"]
        com = json.loads(com)
        article_id = int(com["article_id"])
        content = com["content"]
        c = Comment(article=article_id,content=content,status=0)
        c.owner = request.user
        c.save()
        if c.save():
             a = "ok"
             json_response(a)
        else:
            a = "err"
            json_response(a)
