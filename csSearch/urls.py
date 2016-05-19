from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns(
    'csSearch.views',

    url(r'^search/$','search'),
    url(r'^cssou/$', 'cssou')
)
