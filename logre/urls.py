from django.conf.urls import patterns,include, url
from django.contrib import admin

urlpatterns = patterns(
    'logre.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$','login'),
    url(r'^regeister/$','regeister'),
    url(r'^logout/$','logout'),
)
