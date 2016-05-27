#coding:utf-8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from logre.models import Author
import datetime

# Create your views here.
@csrf_exempt
def login(request):
    global referrer,name
    if request.method == "POST":         #如果是post请求的话
        name = request.POST.get('account')       #获取用户名和密码
        pwd = request.POST.get('password')
        if not Author.objects.filter(author_name = name): #验证用户名和密码
            return render_to_response("logre/login.html", {"error": "该用户不存在，请先注册"})
        elif not Author.objects.filter(author_name = name,author_pwd=pwd):
            return render_to_response("logre/login.html", {"error": "密码不正确，请重新输入"})
        request.session["username"] = name        #将用户和密码信息写入session表
        request.session["pwd"] = pwd
        # print  request.session["username"],request.session["pwd"]
        #手动设置，value=0即关闭浏览器就失效
        if not request.POST.get('check'):
            request.session.set_expiry(0)
        try:
            return HttpResponseRedirect(referrer)
        except:
            return render_to_response("index.html",{'name':name,'pwd':pwd})
    else:
        try:
            referrer=request.META['HTTP_REFERER']  #获取网页访问来源
        except:
            pass
        finally:
            return render_to_response("logre/login.html", {})

@csrf_exempt
def regeister(request):
    global referrer
    if request.method == "POST":
        name = request.POST.get('name')
        #验证用户名是否存在
        if Author.objects.filter(author_name = name):
            return render_to_response("logre/regeister.html", {"error": "该用户名已注册"})
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        #将新注册的用户存入数据库
        author = Author(author_name = name,author_pwd = pwd,author_eamil=email,author_time=time)
        author.save()
        #将信息写入session表
        request.session["username"] = name
        request.session["pwd"] = pwd
        request.session.set_expiry(0)
        try:
            #return HttpResponseRedirect(referrer  + name)
            return HttpResponseRedirect(referrer)
        except:
            return render_to_response("index.html",{'name':name,'pwd':pwd})
    else:
        try:
            #获取网页访问来源
            referrer=request.META['HTTP_REFERER']
            return render_to_response("logre/regeister.html", {})
        except:
            return render_to_response("logre/regeister.html", {})


def logout(request):
    #获取网页访问来源
    referrer=request.META['HTTP_REFERER']
    try:
        del request.session["username"]
        del request.session["pwd"]
        return HttpResponseRedirect(referrer)
    except:
        return HttpResponseRedirect(referrer)
