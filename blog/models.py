#coding:utf-8

from django.db import models
from logre.models import Author

# Create your models here.

class Cate(models.Model):
    cate_name = models.CharField(verbose_name="类别",max_length=20)
    cate_time = models.DateTimeField(verbose_name="添加时间")
    cate_num = models.IntegerField(verbose_name="类别编号")
    def __unicode__(self):      #后台显示的标题
        return self.cate_name
    class Meta:                #定义数据表的名称
        db_table = "blog_cate"

class Blog(models.Model):
    blog_title = models.CharField(blank=False,verbose_name="标题",max_length=20,unique=True)
    #blank = False 表示该项必选
    blog_time = models.DateTimeField(verbose_name="发表时间")
    blog_author = models.ForeignKey(Author,related_name="blog_author",verbose_name="作者")
    blog_cate = models.ForeignKey(Cate,related_name="blog_cate",verbose_name="类别")
    blog_content = models.TextField(blank=False,verbose_name="内容")
    blog_seenum = models.IntegerField(verbose_name="浏览量",default=0)
    blog_id = models.CharField(verbose_name="博客编号",max_length=20,unique=True)

    def __unicode__(self):
        return self.blog_title
    class Meta:
        db_table = "blog"
