#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from item.models import item
from talking.models import talk
from django.views.decorators.csrf import csrf_exempt
import time
# Create your views here.

def home(request):
    item_list = item.objects.all()
    paginator = Paginator(item_list, 6)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        all_item = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_item = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_item = paginator.page(paginator.num_pages)

    return render(request, 'item.html', {
        'all_item': all_item,
    })

@csrf_exempt
def one(request,itemid):
    error = ""
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        # 判断name和email是否唯一
        if talk.objects.filter(talk_name=name, talk_tag=itemid):
            error = "用户名已存在"
        elif talk.objects.filter(talk_email=email, talk_tag=itemid):
            error = "邮箱已存在"
        else:
            content = request.POST.get('content')
            talktime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            talkone = talk(talk_tag=itemid, talk_time=talktime, talk_name=name, talk_email=email, talk_content=content)
            talkone.save()
    # get all talk
    talk_list = talk.objects.filter(talk_tag=itemid).order_by("-talk_time")

    item_mess = item.objects.get(item_id=itemid)
    # update seenum
    item_mess.item_seenum = item_mess.item_seenum + 1
    item_mess.save()
    return render_to_response("item_one_page.html",{
        "item_mess":item_mess,
        "talk_list":talk_list,
        "error":error,
    })