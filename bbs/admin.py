#coding:utf8
from django.contrib import admin
from bbs.models import bbsCate,bbs
# Register your models here.

class bbsCateAmin(admin.ModelAdmin):
    list_display = ('bc_title','bc_num',)     #自定义列表
    list_filter = ('bc_title','bc_num',)      #过滤段
    search_fields = ('bc_title','bc_num',)   #快速查询栏
    fields = ('bc_title','bc_time','bc_num',)       #自定义过滤菜单
    ordering = ('-bc_time',)        #排序

admin.site.register(bbsCate,bbsCateAmin)


class bbsAdmin(admin.ModelAdmin):
    list_display = ('bbs_title','bbs_num','bbs_time','bbs_author','bbs_cate','bbs_seenum',)
    list_filter = ('bbs_title','bbs_num','bbs_time','bbs_author','bbs_cate','bbs_seenum',)
    search_fields = ('bbs_title','bbs_num','bbs_time','bbs_author','bbs_cate','bbs_seenum','bbs_content',)
    fields = ('bbs_title','bbs_num','bbs_time','bbs_author','bbs_cate','bbs_seenum','bbs_content',)
    ordering = ('-bbs_time',)

    #引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
        )

admin.site.register(bbs,bbsAdmin)
