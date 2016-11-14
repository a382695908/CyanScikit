#-*-coding:utf-8-*-
from django.db import models

# Create your models here.
class talk(models.Model):
    #当该条评论信息属于blog或者item时，这里的talk_tag是其对应的id
    talk_tag = models.CharField(blank=False,max_length=64,default="talk",verbose_name="归属")
    talk_time = models.DateTimeField(blank=False,verbose_name="评论时间")
    talk_name = models.CharField(blank=False,max_length=32,verbose_name='昵称')
    talk_email = models.EmailField(blank=False,verbose_name="邮箱")
    talk_content = models.TextField(blank=False,verbose_name="评论内容")

    def __str__(self):
        return self.talk_email
    class Meta:
        db_table = "talking"