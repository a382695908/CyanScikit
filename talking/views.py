#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from talking.models import talk
import time
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def home(request):
    error = ""
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # 判断name和email是否唯一
        if talk.objects.filter(talk_name=name,talk_tag="talk"):
            error="用户名已存在"
        elif talk.objects.filter(talk_email=email,talk_tag="talk"):
            error = "邮箱已存在"
        else:
            content = request.POST.get('content')
            talktime =  time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            talkone = talk(talk_tag="talk",talk_time=talktime,talk_name=name,talk_email=email,talk_content=content)
            talkone.save()

    talk_list = talk.objects.filter(talk_tag="talk").order_by("-talk_time")
    paginator = Paginator(talk_list, 10)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        talks = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        talks = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        talks = paginator.page(paginator.num_pages)
    return render_to_response("talk.html",{
        "talks":talks,
        "error":error,
        "len_list":range(1,paginator.num_pages ),
    })