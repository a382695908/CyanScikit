#coding:utf-8
from django.contrib import admin
from download.models import ResCate,Resource
# Register your models here.

class ResCateAdmin(admin.ModelAdmin):
    list_display = ('resc_title','resc_time','resc_num',)     #自定义列表
    list_filter = ('resc_title','resc_time','resc_num',)      #过滤段
    search_fields = ('resc_title','resc_time','resc_num',)    #快速查询栏
    fields = ('resc_title','resc_time','resc_num',)       #自定义过滤菜单

    ordering = ('-resc_time','resc_num',)

admin.site.register(ResCate,ResCateAdmin)

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('res_title','res_time','res_author','res_cate','res_url','res_seenum','res_downnum')
    list_filter =  ('res_title','res_time','res_author','res_cate','res_url','res_seenum','res_downnum')
    search_fields = ('res_title','res_time','res_author','res_cate','res_url','res_seenum','res_downnum')
    fields = ('res_title','res_time','res_author','res_cate','res_url','res_seenum','res_downnum')

    ordering = ('-res_time','res_seenum','res_downnum',)

admin.site.register(Resource,ResourceAdmin)