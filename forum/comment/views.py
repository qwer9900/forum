from django.shortcuts import render
from .models import Comment
from pyTojs import json_response
from article.models import Article
from message.models import Message
import json
def comment(request):
    if request.method == "POST":
        article_id = int(request.POST.get("article_id"))
        article = Article.objects.get(id=article_id)
        content = request.POST.get("comment")
        current_no = request.POST.get("current_no")
        to_comment_id = int(request.POST.get("to_comment_id",0))
        c = Comment(article=article,content=content,status=0)
        c.owner = request.user
        if to_comment_id != 0:
            to_comment = Comment.objects.get(id=to_comment_id)
        else:
            to_comment = None
        c.to_comment = to_comment
        c.save()
        if c.to_comment:
            msg = Message(owner=c.to_comment.owner,status=-1)
            msg.content = "{}回复了你的评论:{}".format(c.owner,c.to_comment.content)
            msg.link = "{}?page_no={}".format(c.article.id,current_no)
        else:
            msg = Message(owner=c.article.owner,status=-1)
            msg.content = "{}回复了你的文章;{}".format(c.owner,c.article.title)
            msg.link = "{}?page_no={}".format(c.article.id,current_no)
        msg.save()
        if Comment.objects.filter(id=c.id):
             a = {"status":"ok"}
             return json_response(a)
        else:
            a = "err"
            return json_response(a)
