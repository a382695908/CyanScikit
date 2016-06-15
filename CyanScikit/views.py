from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import Blog
from bbs.models import bbs
from download.models import Resource
from logre.models import Author

def index(request):
    blog_list = Blog.objects.all().order_by('-blog_time')[:4]
    resource_list = Resource.objects.all().order_by('-res_seenum')[:10]
    bbs_list = bbs.objects.all().order_by("-bbs_time")[:10]
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]

        t = loader.get_template('index/index.html')
        c = Context({
            "blog_list":blog_list,
            "resource_list":resource_list,
            "bbs_list":bbs_list,
            "name":name,
            "pwd":pwd,
        })
        return HttpResponse(t.render(c))
    except:
        t = loader.get_template('index/index.html')
        blog_list = Blog.objects.all().order_by('-blog_time')[:4]
        resource_list = Resource.objects.all().order_by('res_seenum')[:10]
        c = Context({
            "blog_list":blog_list,
            "resource_list":resource_list,
            "bbs_list":bbs_list,
        })
        return HttpResponse(t.render(c))