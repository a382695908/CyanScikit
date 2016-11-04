#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
#blog cate
class cate(models.Model):
    cate_name = models.CharField(blank=False, max_length=30, verbose_name="美文类别")  # False表示此项不能为空
    cate_addtime = models.DateTimeField(blank=True, verbose_name="类别添加时间")
    cate_id = models.IntegerField(blank=False, verbose_name="类别编号", unique=True)  # 保证编号唯一
    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.cate_name
    class Meta:
        db_table = "blog_cate"


# blog
class blog(models.Model):
    blog_title = models.CharField(blank=False, max_length=30, verbose_name="文章标题")
    blog_id = models.CharField(blank=False, max_length=64, verbose_name="文章唯一ID", unique=True)
    # related_name定义主表对象查询子表时使用的方法名称
    blog_category = models.ForeignKey(cate, blank=False, verbose_name="类别", related_name="article_cate")
    blog_seenum = models.IntegerField(verbose_name="浏览次数", blank=False)  # True表示可不填
    blog_time = models.DateTimeField(blank=False, verbose_name="发表时间")
    blog_content = models.TextField(blank=False, verbose_name="文章内容")
    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.blog_title
    class Meta:
        db_table = "blog"
