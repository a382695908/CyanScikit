#coding:utf8
from django.contrib import admin
from csMarket.models import bigCate,smallCate,Message

# Register your models here.
class bigCateAdmin(admin.ModelAdmin):
    list_display = ('bcate_name','bcate_num','bcate_time',)     #自定义列表
    list_filter = ('bcate_name','bcate_num','bcate_time',)      #过滤段
    search_fields = ('bcate_name','bcate_num','bcate_time',)    #快速查询栏
    fields = ('bcate_name','bcate_num','bcate_time',)       #自定义过滤菜单
    ordering = ('-bcate_time',)        #排序

admin.site.register(bigCate,bigCateAdmin)

class smallCateAdmin(admin.ModelAdmin):
    list_display = ('scate_name','scate_bcate','scate_num','scate_time',)     #自定义列表
    list_filter = ('scate_name','scate_bcate','scate_num','scate_time',)      #过滤段
    search_fields = ('scate_name','scate_bcate','scate_num','scate_time',)    #快速查询栏
    fields = ('scate_name','scate_bcate','scate_num','scate_time',)       #自定义过滤菜单
    ordering = ('-scate_time',)        #排序

admin.site.register(smallCate,smallCateAdmin)

class messageAdmin(admin.ModelAdmin):
    list_display = ('m_num','m_name','m_price','m_from','m_cate_xuorfu','m_bigcate','m_smallcate','m_tuoing','m_to','m_time','m_seenum','m_result','m_content')
    list_filter = ('m_num','m_name','m_price','m_from','m_cate_xuorfu','m_bigcate','m_smallcate','m_tuoing','m_to','m_time','m_seenum','m_result','m_content')
    search_fields = ('m_num','m_name','m_price','m_from','m_cate_xuorfu','m_bigcate','m_smallcate','m_tuoing','m_to','m_time','m_seenum','m_result','m_content')
    fields = ('m_num','m_name','m_price','m_from','m_cate_xuorfu','m_bigcate','m_smallcate','m_to','m_tuoing','m_time','m_seenum','m_result','m_content')
    ordering = ('-m_time',)

admin.site.register(Message,messageAdmin)