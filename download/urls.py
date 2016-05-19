from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns(
    'download.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^download/$', 'download'),
    url(r'^onecateDown/(\w+)/$', 'onecateDown'),
    url(r'^more/$', 'more'),
 )
