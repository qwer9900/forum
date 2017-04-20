from django.shortcuts import render
from .models import Comment
from pyTojs import json_response
from article.models import Article
import json
def comment(request):
    if request.method == "POST":
        article_id = int(request.POST.get("article_id"))
        article = Article.objects.get(id=article_id)
        content = request.POST.get("comment")
        print(content)
        c = Comment(article=article,content=content,status=0)
        c.owner = request.user
        c.save()
        if Comment.objects.filter(article=article):
             a = {"status":"ok"}
             return json_response(a)
        else:
            a = "err"
            return json_response(a)
