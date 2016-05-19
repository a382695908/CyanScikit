from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns(
    'blog.views',
    url(r'^blog/$', 'blog'),
    url(r'^oneblog/(\w+)/$', 'oneblog'),
    url(r'^cateblog/(\d+)/$', 'cateblog'),
    url(r'^more/$', 'more')
)
