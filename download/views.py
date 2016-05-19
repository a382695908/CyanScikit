from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from download.models import Resource,ResCate

# Create your views here.

def download(request):
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('download.html')
        resource_list = Resource.objects.all().order_by('-res_time')[:10]
        c = Context({
            "resource_list":resource_list,
            "name":name,
            "pwd":pwd,
        })
        return HttpResponse(t.render(c))
    except:
        t = loader.get_template('download.html')
        resource_list = Resource.objects.all().order_by('-res_time')[:10]
        c = Context({
            "resource_list":resource_list,
        })
        return HttpResponse(t.render(c))

def onecateDown(request,rescnum):
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]

        t = loader.get_template('download.html')
        rescid = ResCate.objects.get(resc_num=rescnum).id
        resource_list = Resource.objects.filter(res_cate_id=rescid)
        c = Context({
            "resource_list":resource_list,
            "name":name,
            "pwd":pwd,
            "ifmore":1
        })
        return HttpResponse(t.render(c))
    except:
        t = loader.get_template('download.html')
        rescid = ResCate.objects.get(resc_num=rescnum).id
        resource_list = Resource.objects.filter(res_cate_id=rescid)
        c = Context({
            "resource_list":resource_list,
            "ifmore":1
        })
        return HttpResponse(t.render(c))

def more(request):
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        t = loader.get_template('download.html')
        resource_list = Resource.objects.all().order_by('-res_time')
        c = Context({
            "resource_list":resource_list,
            "name":name,
            "pwd":pwd,
            "ifmore":1
        })
        return HttpResponse(t.render(c))
    except:
        t = loader.get_template('download.html')
        resource_list = Resource.objects.all().order_by('-res_time')
        c = Context({
            "resource_list":resource_list,
            "ifmore":1
        })
        return HttpResponse(t.render(c))