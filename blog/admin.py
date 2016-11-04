#-*-coding:utf-8-*-
from django.contrib import admin
from blog.models import cate,blog
# Register your models here.

class adminCate(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("cate_name", "cate_addtime", "cate_id",)
    # 添加search bar，在指定的字段中search
    search_fields = ("cate_name", "cate_addtime",)
    # 页面右边会出现相应的过滤器选项
    list_filter = ("cate_name", "cate_addtime",)
    # 排序
    ordering = ("cate_id",)
admin.site.register(cate,adminCate)

class adminBlog(admin.ModelAdmin):
    # 将字段全部显示出来
    list_display = ("blog_title", "blog_id", "blog_time", "blog_category", "blog_seenum", )
    # 添加search bar，在指定的字段中search
    search_fields = ("blog_time", "blog_category", "blog_seenum",)
    # 页面右边会出现相应的过滤器选项
    list_filter = ("blog_time", "blog_category", "blog_seenum",)
    # 排序
    ordering = ("-blog_time",)
    # 引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
         )

admin.site.register(blog, adminBlog)

