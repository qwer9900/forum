from django.db import models

class Block(models.Model):
    names = models.CharField("板块名称",max_length=100)
    desc = models.CharField("板块描述",max_length=100)
    manager_name = models.CharField("板块管理员名称",max_length=100)
    status = models.IntegerField("状态",choices=((0,"正常"),(-1,"关闭")))
    def __str__(self):
        return self.names
    class Meta:
        verbose_name = "板块"
        verbose_name_plural = "板块配置"
