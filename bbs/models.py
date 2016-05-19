#coding:utf8
from django.db import models
from logre.models import Author
# Create your models here.
class bbsCate(models.Model):
    bc_title = models.CharField(blank=False,verbose_name="标题",max_length=20,unique=True)
    bc_time = models.DateTimeField(verbose_name="发表时间")
    bc_num = models.IntegerField(verbose_name="编号",default=0)

    def __unicode__(self):
        return self.bc_title
    class Meta:
        db_table = "bbscate"

class bbs(models.Model):
    bbs_title = models.CharField(blank=False,verbose_name="标题",max_length=20,unique=True)
    #blank = False 表示该项必选
    bbs_time = models.DateTimeField(verbose_name="发表时间")
    bbs_author = models.ForeignKey(Author,related_name="bbs_author",verbose_name="发表人")
    bbs_cate = models.ForeignKey(bbsCate,related_name="bbs_cate",verbose_name="类别")
    bbs_content = models.TextField(blank=False,verbose_name="内容")
    bbs_seenum = models.IntegerField(verbose_name="浏览量",default=0)
    bbs_num = models.CharField(verbose_name="编号",max_length=40,default=0)

    def __unicode__(self):
        return self.bbs_title
    class Meta:
        db_table = "bbs"
