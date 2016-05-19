#coding:utf-8

from django.contrib import admin
from blog.models import Blog,Cate
# Register your models here.

class CateAdmin(admin.ModelAdmin):
    list_display = ('cate_name','cate_num','cate_time',)     #自定义列表
    list_filter = ('cate_name','cate_num','cate_time',)      #过滤段
    search_fields = ('cate_name','cate_num','cate_time',)    #快速查询栏
    fields = ('cate_name','cate_num','cate_time',)       #自定义过滤菜单
    ordering = ('-cate_time',)        #排序

admin.site.register(Cate,CateAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title','blog_id','blog_time','blog_author','blog_cate','blog_seenum')
    list_filter = ('blog_title','blog_id','blog_time','blog_author','blog_cate','blog_seenum')
    search_fields = ('blog_title','blog_id','blog_time','blog_author','blog_cate','blog_seenum')
    fields = ('blog_title','blog_id','blog_time','blog_author','blog_cate','blog_content','blog_seenum')
    ordering = ('-blog_time',)

    #引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
        )

admin.site.register(Blog,BlogAdmin)
