from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ("owner","article","content","status","to_comment","create_timestamp","last_timestamp")
admin.site.register(Comment,CommentAdmin)
