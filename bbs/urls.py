from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns(
    'bbs.views',
    url(r'^newone/(\w+)/$', 'newone'),
    url(r'^news/$', 'news'),
    url(r'^newcate/(\w+)/$', 'newcate'),
    url(r'^more/$','more')
)
