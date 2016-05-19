#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,Context
from blog.models import Blog,Cate

# Create your views here.

def blog(request):
    blog_list = Blog.objects.all().order_by("-blog_time")[:8]
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]

        t = loader.get_template('blog.html')
        c = Context({
            "blog_list":blog_list,
            "name":name,
            "pwd":pwd,
        })
        return HttpResponse(t.render(c))
    except:
        t = loader.get_template('blog.html')
        c = Context({
            "blog_list":blog_list,
        })
        return HttpResponse(t.render(c))


def oneblog(request,bid):
    t = loader.get_template('oneblog.html')
    blog = Blog.objects.get(blog_id=bid)
    new_seenum = blog.blog_seenum+1
    Blog.objects.filter(blog_id=bid).update(blog_seenum = new_seenum)
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]

        c = Context({
            "blog":blog,
            "name":name,
            "pwd":pwd,
        })
        return HttpResponse(t.render(c))
    except:
        return render_to_response("oneblog.html",{
            "blog":blog,
        })



def cateblog(request,catenum):
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]

        bcateid = Cate.objects.get(cate_num=catenum).id
        blog_list = Blog.objects.filter(blog_cate_id=bcateid)
        return render_to_response('cateblog.html',{
            'blog_list':blog_list,
            "name":name,
            "pwd":pwd,
        })
    except:
        bcateid = Cate.objects.get(cate_num=catenum).id
        blog_list = Blog.objects.filter(blog_cate_id=bcateid)
        return render_to_response('cateblog.html',{
            'blog_list':blog_list
        })

def more(request):
    blog_list = Blog.objects.all().order_by("-blog_time")[8:]
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('blog.html')
        c = Context({
            "blog_list":blog_list,
            "name":name,
            "pwd":pwd,
            "ifmore":1,
        })
        return HttpResponse(t.render(c))
    except:
        t = loader.get_template('blog.html')
        c = Context({
            "blog_list":blog_list,
            "ifmore":1,
        })
        return HttpResponse(t.render(c))