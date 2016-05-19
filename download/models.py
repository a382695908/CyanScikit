#coding:utf-8
from django.db import models
from logre.models import Author
# Create your models here.

class ResCate(models.Model):
    resc_title = models.CharField(verbose_name="类别名称",unique=True,max_length=50)
    resc_time = models.DateTimeField(verbose_name="上传时间")
    resc_num = models.IntegerField(verbose_name="类别编号")

    def __unicode__(self):
        return self.resc_title

    class Meta:
        db_table="resource_cate"

class Resource(models.Model):
    res_title = models.CharField(blank=False,verbose_name="资源名称",max_length=30)
    res_time = models.DateTimeField(verbose_name="上传时间")
    res_author = models.ForeignKey(Author,related_name="res_author",verbose_name="上传人")
    res_cate = models.ForeignKey(ResCate,related_name="res_cate",verbose_name="资源类别")
    res_url = models.URLField(blank=False,verbose_name="资源URL")
    res_seenum = models.IntegerField(verbose_name="浏览量",default=0)
    res_downnum = models.IntegerField(verbose_name="下载量",default=0)

    def __unicode__(self):
        return self.res_title

    class Meta:
        db_table="resource"