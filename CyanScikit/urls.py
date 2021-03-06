"""CyanScikit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django import views
from CyanScikit.upload import upload_image
from CyanScikit.views import index
urlpatterns = [
    url(r'^admin/uploads/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r"^uploads/(?P<path>.*)$",views.static.serve,{"document_root":settings.MEDIA_ROOT,}),
    #http://www.imooc.com/qadetail/98920
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', include('index.urls'), name='idnex'),
    url(r'^blog/', include('blog.urls'), name='blog'),
    url(r'^item/', include('item.urls'), name='item'),
    url(r'^market/', include('market.urls'), name='market'),
    url(r'^talking/', include('talking.urls'), name='talking'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^user/', include('user.urls'), name='user'),
    url(r'^$', index,name="index"),
]
