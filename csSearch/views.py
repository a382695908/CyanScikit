#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,Context
from django.views.decorators.csrf import csrf_exempt
from bbs.models import bbs,bbsCate
from blog.models import Blog,Cate
from csMarket.models import Message,bigCate,smallCate
from download.models import Resource
from logre.models import Author
# Create your views here.

import urllib
import urllib2
import re,os

def baidu(kw):
    url = "http://www.baidu.com/s"
    search = [('w',kw )]
    getString = url + "?" + urllib.urlencode(search)

    req = urllib2.Request(getString)
    fd = urllib2.urlopen(req)
    baiduResponse=""
    while 1:
        data= fd.read(1024)
        if not len(data):
            break
        baiduResponse+=data
    fobj=open(r'D:\WWW\CyanScikit\templates\result.html','w')
    fobj.write(baiduResponse)
    fobj.close()

def cssou(request,kw):
    try:
        if request.method=="POST":
            try:
                name = request.session["username"]
                pwd = request.session["pwd"]
            except:
                name = ""
                pwd =""
            finally:
                if request.method=='POST':
                    keyword = request.POST.get('kw').encode("utf-8")
                    scate = request.POST.get("sousuo")
                    if scate =="2":
                        baidu(keyword)
                        return render_to_response('result.html',{"name":name,"pwd":pwd,})
                    else:
                        #执行站内搜搜
                        bbs_list,blog_list,resource_list,message_list = cssou(keyword,keyword)
                        return render_to_response('cssou.html',{
                            "bbs_list":bbs_list,
                            "blog_list":blog_list,
                            "resource_list":resource_list,
                            "message_list":message_list,
                        })
                else:
                    return render_to_response('cssearch.html',{"name":name,"pwd":pwd,})
    except:
        bbs_list = bbs.objects.filter(bbs_title__icontains=kw)
        blog_list=Blog.objects.filter(blog_title__icontains=kw)
        resource_list = Resource.objects.filter(res_title__icontains=kw)
        message_list= Message.objects.filter(m_name__icontains=kw)

        bbs_list = bbs.objects.filter(bbs_title__icontains=kw)|bbs.objects.filter(bbs_cate__bc_title__icontains=kw)|bbs.objects.filter(bbs_content__icontains=kw)

        blog_list = Blog.objects.filter(blog_title__icontains=kw)|Blog.objects.filter(blog_cate__cate_name__icontains=kw)|Blog.objects.filter(blog_content__icontains=kw)

        resource_list = Resource.objects.filter(res_title__icontains=kw)|Resource.objects.filter(res_cate__resc_title__icontains=kw)

        message_list = Message.objects.filter(m_name__icontains=kw)|Message.objects.filter(m_content__icontains=kw)|Message.objects.filter(m_smallcate__scate_name__icontains=kw)|Message.objects.filter(m_bigcate__bcate_name__icontains=kw)
        return bbs_list,blog_list,resource_list,message_list

@csrf_exempt
def search(request):
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
    except:
        name = ""
        pwd =""
    finally:
        if request.method=='POST':
            keyword = request.POST.get('kw').encode("utf-8")
            scate = request.POST.get("sousuo")
            if scate =="2":
                baidu(keyword)
                return render_to_response('result.html',{"name":name,"pwd":pwd,})
            else:
                #执行站内搜搜
                bbs_list,blog_list,resource_list,message_list = cssou(keyword,keyword)
                return render_to_response('cssou.html',{
                    "bbs_list":bbs_list,
                    "blog_list":blog_list,
                    "resource_list":resource_list,
                    "message_list":message_list,
                })
        else:
            return render_to_response('cssearch.html',{"name":name,"pwd":pwd,})
