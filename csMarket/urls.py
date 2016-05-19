from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns(
    'csMarket.views',
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^market/(\w+)/$', 'market'),
    url(r'^market/$', 'market'),
    url(r'^msou/$', 'msou'),

    url(r'^xsMarket/$', 'xsMarket'),
    url(r'^fwMarket/$', 'fwMarket'),
    url(r'^showMarket/$', 'showMarket'),

    url(r'^message/$', 'message'),
    url(r'^messageAlter/(.+)/$', 'messageAlter'),
    url(r'^forall/(\w+)/$', 'forall'),

    url(r'^user/$', 'user'),
    url(r'^userFw/$', 'userFw'),
    url(r'^userOne/(.+)/$', 'userOne'),
    url(r'^userAlter/$', 'userAlter'),
)
