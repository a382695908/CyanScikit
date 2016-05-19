#coding:utf8
from django.db import models
from logre.models import Author


# Create your models here.
class bigCate(models.Model):
    bcate_name = models.CharField(verbose_name="大类别标题",max_length=30)
    bcate_time = models.DateTimeField(verbose_name="添加时间")
    bcate_num = models.IntegerField(verbose_name="大类别编号",unique=True)

    def __unicode__(self):
        return self.bcate_name

    class Meta:
        db_table = "bigcate"

class smallCate(models.Model):
    scate_name = models.CharField(verbose_name="小类别标题",max_length=30)
    scate_time = models.DateTimeField(verbose_name="添加时间")
    scate_num = models.IntegerField(verbose_name="小类别编号",unique=True)
    scate_bcate = models.ForeignKey(bigCate,verbose_name="所属大类别")

    def __unicode__(self):
        return self.scate_name

    class Meta:
        db_table = "smallcate"

class Message(models.Model):
    m_num = models.CharField(verbose_name="信息编号",blank=False,max_length=40,unique=True)
    m_name = models.CharField(verbose_name="信息标题",blank=False,max_length=40)
    m_content = models.TextField(verbose_name="信息内容",blank=False,default="此信息无具体内容",max_length=250)
    m_price = models.FloatField(verbose_name="价格",blank=False,default="")
    m_from = models.CharField(verbose_name="发布方",blank=False,max_length=30)
    m_cate_xuorfu = models.CharField(verbose_name="需求or服务",blank=False,max_length=20,default="需求")
    m_bigcate = models.ForeignKey(bigCate,verbose_name="所属大类别",blank=False)
    m_smallcate = models.ForeignKey(smallCate,verbose_name="所属小类别",blank=False)
    m_tuoing = models.CharField(verbose_name="是否托管",blank=False,max_length=15,default="否")
    m_to = models.ForeignKey(Author,verbose_name="托管方",blank=True,)
    m_result = models.CharField(verbose_name="交易是否成功",blank=False,max_length=20,default="否")
    m_time = models.DateTimeField(verbose_name="发布时间",blank=False)
    m_seenum = models.IntegerField(verbose_name="浏览次数",blank=False,default=0)

    def __unicode__(self):
        return self.m_name

    class Meta:
        db_table = "message"