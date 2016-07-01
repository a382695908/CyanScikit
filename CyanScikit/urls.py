#-*-coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from blog.upload import upload_image
from views import index

urlpatterns = [
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),

    url(r"^uploads/(?P<path>.*)$", \
                "django.views.static.serve", \
                {"document_root": settings.MEDIA_ROOT,}),

    url(r'^admin/', include(admin.site.urls),name='admin'),

    url(r'^bbs/', include('bbs.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^download/', include('download.urls')),
    url(r'^csMarket/', include('csMarket.urls')),
    url(r'^csSearch/', include('csSearch.urls')),
    url(r'^logre/', include('logre.urls')),
    url(r'^index/index/', index,name="index"),
    url(r'^$', index,name="index"),
    ]
'''
name参数的作用是：
1：functions中的redirect传递url可以使用别名
2：模板里面用 {%url url_name 参数%}
'''