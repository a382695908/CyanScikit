#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import blog,cate
from talking.models import talk
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.
#hot blog
def gethot():
    hot_list = blog.objects.all().order_by("-blog_seenum")[:10]
    return hot_list

#cate
def getcate():
    return cate.objects.all()

def home(request):
    blog_list = blog.objects.all()
    paginator = Paginator(blog_list, 8)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        all_blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_blog = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {
        'all_blog': all_blog,
        "cates": getcate(),
        "hot_list":gethot(),
    })
@csrf_exempt
def one(request,id):
    error = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # 判断name和email是否唯一
        if talk.objects.filter(talk_name=name ,talk_tag=id):
            error="用户名已存在"
        elif talk.objects.filter(talk_email=email,talk_tag=id):
            error = "邮箱已存在"
        else:
            content = request.POST.get('content')
            talktime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            talkone = talk(talk_tag=id, talk_time=talktime, talk_name=name, talk_email=email, talk_content=content)
            talkone.save()

    blog_mess = blog.objects.get(blog_id=id)
    #update seenum
    blog_mess.blog_seenum = blog_mess.blog_seenum + 1
    blog_mess.save()
    # get all talk
    talk_list = talk.objects.filter(talk_tag=id).order_by("-talk_time")
    return render_to_response("blog_one_page.html",{
        "blog_mess":blog_mess,
        "cates": getcate(),
        "hot_list":gethot(),
        "error":error,
        "talk_list":talk_list,
    })

def onecate(request,catename):
    cateid = cate.objects.get(cate_name=catename)
    blog_list = blog.objects.filter(blog_category=cateid)
    paginator = Paginator(blog_list, 5)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        all_blog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_blog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_blog = paginator.page(paginator.num_pages)

    return render(request, 'blog.html', {
        'all_blog': all_blog,
        "cates": getcate(),
        "hot_list":gethot(),
    })