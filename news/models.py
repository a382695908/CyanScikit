#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
#news
class news(models.Model):
    news_title = models.CharField(blank=False, max_length=30, verbose_name="新闻标题")
    news_id = models.CharField(blank=False, max_length=64, verbose_name="唯一ID", unique=True)
    # related_name定义主表对象查询子表时使用的方法名称
    news_seenum = models.IntegerField(verbose_name="浏览次数", blank=False)  # True表示可不填
    news_time = models.DateTimeField(blank=False, verbose_name="发表时间")
    news_content = models.TextField(blank=False, verbose_name="新闻内容")
    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.news_title
    class Meta:
        db_table = 'news'
