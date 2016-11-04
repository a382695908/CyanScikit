#-*-coding:utf-8-*-
from django.contrib import admin
from item.models import item
# Register your models here.
class adminItem(admin.ModelAdmin):
    list_display = ('item_title','item_id','item_seenum','item_time',)
    search_fields = ('item_id','item_seenum',)
    list_filter = ('item_seenum','item_time',)
    ordering = ('-item_time',)
    # 引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
            )
admin.site.register(item,adminItem)