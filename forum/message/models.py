from django.db import models
from comment.models import Comment
from django.contrib.auth.models import User
class Message(models.Model):
    owner = models.ForeignKey(User,verbose_name="用户名")
    content = models.CharField("内容",max_length=10)
    status = models.IntegerField("状态",choices=((0,"已读"),(-1,"未读")))
    link = models.CharField("链接",max_length=10)

   
