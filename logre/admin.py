#coding:utf-8
from django.contrib import admin
from logre.models import Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    #'author_img',
    list_display = ('author_name', 'author_phone', 'author_qq', 'author_eamil', 'author_pwd','author_xingqu','author_time',)   #把字段信息全部显示出来
    search_fields = ('author_name', 'author_phone', 'author_qq', 'author_eamil','author_xingqu','author_time',)        #添加search bar，在指定的字段中search
    list_filter = ('author_name',  'author_phone', 'author_qq','author_eamil','author_xingqu','author_time',)   #页面右边会出现相应的过滤器选项
    ordering = ('-author_time',)                #排序


admin.site.register(Author,AuthorAdmin)