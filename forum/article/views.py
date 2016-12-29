from django.shortcuts import render,redirect
from block.models import Block
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator
def article_list(request,block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    ARTICLE_CNT_1PAGE = 1
    page_no = int(request.GET.get("page_no","1"))
    all_articles = Article.objects.filter(block=block,status=0).order_by("-id")
    p = Paginator(all_articles,ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    articles_objs = page.object_list
    page_links = [i for i in range(page_no-5,page_no+6) if i >0 and i <= p.num_pages]
    before = page_links[0]-1
    after = page_links[-1]+1
    next = page_no+1
    last = page_no-1 
    return render(request,"article_list.html",{"articles":articles_objs,"b":block,"p":p,"page_no":page_no,"page_links":page_links,"before":before,"after":after,"next":next,"last":last})
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
            article.status = 0
            article.save()
            return redirect("/article/list/%s" % block_id)
        else:
            return render(request,"create.html",{"b":block,"form":form})
def detail(request,d_id):
    d_id = int(d_id)
    article = Article.objects.get(id=d_id)
    return render(request,"detail.html",{"detail":article,})
