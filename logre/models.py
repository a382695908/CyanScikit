#coding:utf-8
from django.db import models
# Create your models here.

class Author(models.Model):
    author_name = models.CharField(blank=False,max_length=15,verbose_name="姓名")
    author_eamil = models.EmailField(verbose_name="邮箱")
    author_phone = models.CharField(blank=True,verbose_name="电话",max_length=11)
    author_qq = models.CharField(blank=True,verbose_name="QQ",max_length=10)
    author_pwd = models.CharField(blank=False,max_length=50,verbose_name="密码")
    author_time = models.DateTimeField(verbose_name="注册时间")
    author_xingqu = models.CharField(verbose_name="我的兴趣",blank=True,max_length=50)

    def __unicode__(self):
        return self.author_name
    class Meta:
        db_table="author"
