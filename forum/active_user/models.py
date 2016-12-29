from django.db import models
from user.models import User
from django.utils import timezone
from datetime import timedelta
class active_User(models.Model):
    user = models.CharField("用户名",max_length=10)
    active_str = models.CharField("激活码",max_length=100)
    deadline = models.DateTimeField(default = timezone.now() + timedelta(days=1))
    
    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "用户激活"
        verbose_name_plural = "用户激活"

