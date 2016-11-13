#-*-coding:utf-8-*-
from django.contrib import admin
from news.models import news
# Register your models here.


class adminNews(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("news_title", "news_id", "news_seenum", "news_time",)
    # 添加search bar，在指定的字段中search
    search_fields = ("news_title", "news_id", "news_seenum", "news_time",)
    # 页面右边会出现相应的过滤器选项
    list_filter = (  "news_seenum", "news_time",)
    # 排序
    ordering = ("-news_time",)
    # 引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
         )

admin.site.register(news, adminNews)

