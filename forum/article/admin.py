from django.contrib import admin
from comment.models import Comment
from .models import Article 

class CommentInline(admin.TabularInline):
    model = Comment
    can_delete = False
class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
admin.site.register(Article,ArticleAdmin)
