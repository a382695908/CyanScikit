#-*-coding:utf-8-*-
from django.contrib import admin
from talking.models import talk
# Register your models here.

class adminTalk(admin.ModelAdmin):
    list_display = ('talk_tag','talk_time','talk_name','talk_email','talk_content',)
    search_fields = ('talk_tag','talk_time','talk_name','talk_email',)
    list_filter = ('talk_tag','talk_time','talk_name','talk_email',)
    ordering = ('-talk_time',)

    # 引入媒体文件 文本编辑器
    class Media:
        js = (
            '/static/js/kindeditor-4.1.7/kindeditor-min.js',
            '/static/js/kindeditor-4.1.7/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.7/config.js',
        )
admin.site.register(talk,adminTalk)


