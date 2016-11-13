#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
#外包类别
class wcate(models.Model):
    wcate_name = models.CharField(blank=False, max_length=30, verbose_name="外包类别")  # False表示此项不能为空
    wcate_addtime = models.DateTimeField(blank=True, verbose_name="类别添加时间")
    wcate_people = models.TextField(blank=False, default="",verbose_name="负责人介绍")
    wcate_id = models.IntegerField(blank=False, verbose_name="类别编号", unique=True)  # 保证编号唯一
    wcate_content = models.TextField(blank=False, verbose_name="类别介绍")
    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.wcate_name
    class Meta:
        db_table = "waibao_cate"

class example(models.Model):
    ex_title = models.CharField(blank=False, max_length=30, verbose_name="案例标题")
    ex_id = models.CharField(blank=False, max_length=64, verbose_name="唯一ID", unique=True)
    # related_name定义主表对象查询子表时使用的方法名称
    ex_category = models.ForeignKey(wcate, blank=False, verbose_name="类别", related_name="article_cate")
    ex_seenum = models.IntegerField(verbose_name="浏览次数", blank=False)  # True表示可不填
    ex_money =models.IntegerField(verbose_name="成交金额",blank=True)
    ex_gree = models.FloatField(verbose_name="满意度",blank=True)
    ex_time = models.DateTimeField(blank=False, verbose_name="发表时间")
    ex_content = models.TextField(blank=False, verbose_name="案例描述")

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.ex_title

    class Meta:
        db_table = "example"