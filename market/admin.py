#-*-coding:utf-8-*-
from django.contrib import admin
from market.models import wcate,example

# Register your models here.
class adminWcate(admin.ModelAdmin):
    list_display = ('wcate_name','wcate_addtime','wcate_id',)
    search_fields = ('wcate_name','wcate_addtime','wcate_id',)
    list_filter = ('wcate_name','wcate_addtime','wcate_id',)
    ordering = ('-wcate_addtime',)

    # 引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
        )
admin.site.register(wcate,adminWcate)

class adminExample(admin.ModelAdmin):
    list_display = ('ex_title','ex_id','ex_money','ex_gree','ex_category','ex_seenum','ex_time',)
    search_fields = ('ex_id','ex_category','ex_money','ex_gree','ex_seenum','ex_time',)
    list_filter = ('ex_id','ex_category','ex_money','ex_gree','ex_seenum','ex_time',)
    ordering = ('-ex_time',)
    # 引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
        )
admin.site.register(example,adminExample)

