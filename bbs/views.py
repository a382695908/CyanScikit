from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader,Context
from bbs.models import bbs,bbsCate

# Create your views here.

def news(request):
    bbs_list = bbs.objects.all().order_by("-bbs_time")[:8]
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('bbs.html')
        c = Context({
            "name":name,
            "pwd":pwd,
            "bbs_list":bbs_list,
        })
        return HttpResponse(t.render(c))
    except:
        return render_to_response("bbs.html",{
            "bbs_list":bbs_list
        })

def newcate(request,id):
    bid = bbsCate.objects.get(bc_num=id).id
    bbs_list = bbs.objects.filter(bbs_cate_id=bid).order_by("-bbs_time")[:10]
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('bbs.html')
        c = Context({
            "name":name,
            "pwd":pwd,
            "bbs_list":bbs_list,
        })
        return HttpResponse(t.render(c))
    except:
        return render_to_response("bbs.html",{
            "bbs_list":bbs_list
        })

def newone(request,id):
    one = bbs.objects.get(bbs_num=id)
    one.bbs_seenum = one.bbs_seenum+1
    one.save()
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('newone.html')
        c = Context({
            "name":name,
            "pwd":pwd,
            "one":one,
        })
        return HttpResponse(t.render(c))
    except:
        bbs_list = bbs.objects.all().order_by("-bbs_time")[:8]
        return render_to_response("newone.html",{
            "bbs_list":bbs_list,
            "one":one,
        })

def more(request):
    bbs_list = bbs.objects.all().order_by("-bbs_time")[8:]
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('bbs.html')
        c = Context({
            "name":name,
            "pwd":pwd,
            "bbs_list":bbs_list,
            "ifmore":1
        })
        return HttpResponse(t.render(c))
    except:
        return render_to_response("bbs.html",{
            "bbs_list":bbs_list,
            "ifmore":1
        })