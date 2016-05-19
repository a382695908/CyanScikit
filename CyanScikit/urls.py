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

    url(r'^admin/', include(admin.site.urls)),

    url(r'^bbs/', include('bbs.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^download/', include('download.urls')),
    url(r'^csMarket/', include('csMarket.urls')),
    url(r'^csSearch/', include('csSearch.urls')),
    url(r'^logre/', include('logre.urls')),
    url(r'^index/index/', index),
    url(r'^$', index),
    ]
