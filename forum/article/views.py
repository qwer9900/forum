from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from tools import paginate_queryset
from comment.views import comment
from comment.models import Comment
def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    ARTICLE_CNT_1PAGE = 1
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    articles_objs,page = paginate_queryset(all_articles,page_no,1)
    return render(request,"article_list.html",{"articles":articles_objs,"b":block,"page":page})
@login_required
def createAppear(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request,"create.html",{"b":block,})
    else:
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.block = block
            article.owner = request.user
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request,"create.html",{"b":block,"form":form})
def detail(request,d_id):
    d_id = int(d_id)
    article = Article.objects.get(id=d_id)
    page_no = int(request.GET.get("page_no","1"))
    all_comments = Comment.objects.filter(article=d_id,status=0).order_by("-id")
    comments_objs,page = paginate_queryset(all_comments,page_no,1)
    return render(request,"detail.html",{"detail":article,"page":page,"comments":comments_objs})
