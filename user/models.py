from django.db import models
import hashlib

# Create your models here.
class User(models.Model):
    user_name = models.CharField(blank=False, max_length=15, verbose_name="用户名")
    user_head_img = models.ImageField() #用户头像
    user_sex = models.BooleanField(max_length=1, choices=((0, '男'),(1, '女'),), verbose_name="性别")
    user_birth = models.DateField(blank=True, verbose_name="出生年月")
    user_passwd = models.CharField(blank=False, max_length=15, verbose_name="密码")
    user_phone = models.CharField(blank=True, max_length=11, verbose_name="电话")
    user_email = models.EmailField(blank=False, verbose_name="邮箱")
    user_interest = models.CharField(blank= True, max_length=60, verbose_name="兴趣爱好")
    user_created_time = models.DateTimeField(verbose_name="注册时间")
    user_updated_time = models.DateTimeField(verbose_name="更新时间")

    #进行身份验证的信息
    user_real_name = models.CharField()
    user_card_number = models.CharField()
    user_xueli = models.CharField()
    user_college = models.CharField(blank=True, max_length=30, verbose_name="大学名称")
    user_academy = models.CharField()
    user_major = models.CharField()
    user_class = models.CharField()
    user_number = models.CharField()
    user_start_year =models.DateField()
    user_end_year = models.DateField()
    user_zheng_img = models.ImageField()  #学生证照片

    # python 2.7中使用的是__unicode__
    def __str__(self):
        return self.news_title

    class Meta:
        db_table = 'users'

    # def save(self, *args, **kwargs):
    #     self.passwd = hashlib.sha1(self.user_passwd + self.user_name).hexdigest()
    #     super(User, self).save(*args, **kwargs)
