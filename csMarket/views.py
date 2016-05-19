#coding:utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,Context
from logre.models import Author
from csMarket.models import bigCate,smallCate
from csMarket.models import Message
from bbs.models import bbs
from blog.models import Blog
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import  random,uuid,datetime
import tongji

def msou(request):
    xs_message_list = Message.objects.filter(m_cate_xuorfu="需求").order_by("-m_time")[:8]
    fw_message_list = Message.objects.filter(m_cate_xuorfu="服务").order_by("-m_time")[:8]
    message1_list = Message.objects.filter(m_result = "是").order_by("-m_time")[:8]
    t = loader.get_template('marketall.html')
    keyword = request.POST.get('kw').encode("utf-8")
    message_list = Message.objects.filter(m_name__icontains=keyword) | Message.objects.filter(m_content__icontains=keyword) | Message.objects.filter(m_smallcate__scate_name__icontains=keyword) |Message.objects.filter(m_bigcate__bcate_name__icontains=keyword)
    print len(message_list)
    if len(message_list)==0:
        error = "11"
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            author = Author.objects.get(author_name=name)
            return render_to_response("csmarket.html",({
                "error":error,
                'name':name,
                'pwd':pwd,
                "author":author,
                "xs_message_list":xs_message_list,
                "fw_message_list":fw_message_list,
                "message_list":message1_list,}))
        except:
                return render_to_response("csmarket.html",({
                "error":error,
                "xs_message_list":xs_message_list,
                "fw_message_list":fw_message_list,
                "message_list":message1_list,}))
    else:
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            author = Author.objects.get(author_name=name)
            c = Context({
            "title":"你搜索-> " + keyword + " <-的结果为：",
            'name':name,
            'pwd':pwd,
            "author":author,
            "message_list":message_list,
            })
        except:
            c = Context({
            "title":"你搜索-> " + keyword + " <-的结果为：",
            "message_list":message_list,
            })
        return HttpResponse(t.render(c))

@csrf_exempt
def market(request):
    if request.method=="POST":
        return msou(request)
    else:
        t = loader.get_template('csmarket.html')
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            author = Author.objects.get(author_name=name)

            xs_message_list = Message.objects.filter(m_cate_xuorfu="需求").order_by("-m_time")[:8]
            fw_message_list = Message.objects.filter(m_cate_xuorfu="服务").order_by("-m_time")[:8]
            message_list = Message.objects.filter(m_result = "是").order_by("-m_time")[:8]
            c = Context({
            'name':name,
            'pwd':pwd,
            "author":author,
            "xs_message_list":xs_message_list,
            "fw_message_list":fw_message_list,
            "message_list":message_list,
            })
            return HttpResponse(t.render(c))
        except:
            xs_message_list = Message.objects.filter(m_cate_xuorfu="需求").order_by("-m_time")[:8]
            fw_message_list = Message.objects.filter(m_cate_xuorfu="服务").order_by("-m_time")[:8]
            message_list = Message.objects.filter(m_result = "是").order_by("-m_time")[:8]
        return render_to_response("csmarket.html",{
            "xs_message_list":xs_message_list,
            "fw_message_list":fw_message_list,
            "message_list":message_list,})

@csrf_exempt
def xsMarket(request):
    if request.method=="POST":
        return msou(request)
    else:
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]

            message_list = Message.objects.filter(m_cate_xuorfu="需求").order_by("-m_time")[:16]
            return render_to_response("marketall.html",{
                "title":"悬赏大厅",
                'name':name,
                'pwd':pwd,
                "message_list":message_list,
            })
        except:
            message_list = Message.objects.filter(m_cate_xuorfu="需求").order_by("-m_time")[:8]
            return render_to_response("marketall.html",{
                "title":"悬赏大厅",
                "message_list":message_list,})

@csrf_exempt
def fwMarket(request):
    if request.method=="POST":
        return msou(request)
    else:
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            message_list = Message.objects.filter(m_cate_xuorfu="服务").order_by("-m_time")[:16]
            return render_to_response("marketall.html",{
                "title":"服务商库",
                'name':name,
                'pwd':pwd,
                "message_list":message_list,
            })
        except:
            message_list = Message.objects.filter(m_cate_xuorfu="服务").order_by("-m_time")[:16]
            return render_to_response("marketall.html",{
                "title":"服务商库",
                "message_list":message_list,})

@csrf_exempt
def showMarket(request):
    if request.method=="POST":
        return msou(request)
    else:
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            message_list = Message.objects.filter(m_result="是").order_by("-m_time")[:16]
            return render_to_response("marketall.html",{
                "title":"作品展示",
                'name':name,
                'pwd':pwd,
                "message_list":message_list,
            })
        except:
            message_list = Message.objects.filter(m_result="是").order_by("-m_time")[:16]
            return render_to_response("marketall.html",{
                "title":"作品展示",
                "message_list":message_list,})

#发布服务
@csrf_exempt
def message(request):
    hot_list = Message.objects.filter(m_tuoing="否").order_by("-m_seenum")[:6]
    jin_list = Message.objects.all()[:6]
    news_list = bbs.objects.all().order_by("-bbs_time")[:6]
    moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing=tongji.tongji(request)

    try:
        name = request.POST.get('account')
        pwd = request.POST.get('password')
        author = Author.objects.get(author_name = name)
    except:
        pass

    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        author = Author.objects.get(author_name = name)
        xingqu = Author.objects.get(author_name=name).author_xingqu
        like_list = Message.objects.filter(m_bigcate__contains=xingqu) | Message.objects.filter(m_smallcate__contains=xingqu)
        like_list = like_list[:6]
    except:
        like_list = Message.objects.all()[:6]

    if request.method=="POST":
        try:
            num = uuid.uuid4()
            title = request.POST.get("title")
            price = request.POST.get("price")
            cate = request.POST.get("mcate")
            bigcate = request.POST.get("bigcate")
            smallcate = request.POST.get("smallcate")
            bid = bigCate.objects.get(bcate_name=bigcate).id
            sid = smallCate.objects.get(scate_name=smallcate).id
        except:
             return render_to_response("csmarket.html", {
                "title":"",
                'name':name,
                'pwd':pwd,
                "author":author,
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
                "news_list":news_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
                })

        try:
            prince = int(price)-1
        except:
            error = "price只能为数字"
            return render_to_response("message.html",{
                "error":error,
                "name":name,
                "pwd":pwd,
                "author":author,
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
                 "news_list":news_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
            })
        try:
            tuo = request.POST.get("toone")
            toid = Author.objects.get(author_name=tuo)
        except:
            error = "托管方不存在"
            return render_to_response("message.html",{
                "error":error,
                "name":name,
                "pwd":pwd,
                "author":author,
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
                 "news_list":news_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
            })
        mtuo = request.POST.get("mtuo")
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        result = request.POST.get("mresult")
        content = request.POST.get("content")
        mm = Message(m_num=num,m_name=title,m_price=price,m_from=name,m_content=content,m_cate_xuorfu=cate,m_bigcate_id=bid,\
                     m_smallcate_id=sid,m_tuoing=mtuo,m_to_id=2,m_result=result,m_time=time)

        mm.save()
        return render_to_response("userone.html",{
            "name":name,
            "pwd":pwd,
            "author":author,
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "message":mm,
            "news_list":news_list,
            "moneyin":moneyin,
            "moneyout":moneyout,
            "mxuok":mxuok,
            "mfwok":mfwok,
            "mxu":mxu,
            "mfw":mfw,
            "mxuing":mxuing,
            "mfwing":mfwing
        })

    else:
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            author = Author.objects.get(author_name=name)
            return render_to_response("message.html", {
            "title":"",
            'name':name,
            'pwd':pwd,
            "author":author,
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "news_list":news_list,
            "moneyin":moneyin,
            "moneyout":moneyout,
            "mxuok":mxuok,
            "mfwok":mfwok,
            "mxu":mxu,
            "mfw":mfw,
            "mxuing":mxuing,
            "mfwing":mfwing
            })
        except:
            return render_to_response("logre/login.html", {
                "error":"你还没有登录,请先登录",
            })


@csrf_exempt
def messageAlter(request,id):

    mm = Message.objects.get(m_num=id)
    hot_list = Message.objects.filter(m_tuoing="否").order_by("-m_seenum")[:6]
    jin_list = Message.objects.all()[:6]
    news_list = bbs.objects.all().order_by("-bbs_time")[:8]

    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        author = Author.objects.get(author_name = name)
        xingqu = Author.objects.get(author_name=name).author_xingqu
        like_list = Message.objects.filter(m_bigcate__contains=xingqu) | Message.objects.filter(m_smallcate__contains=xingqu)
        like_list = like_list[:6]
    except:
        like_list = Message.objects.all()[:6]

    moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing=tongji.tongji(request)

    if request.method=="POST":

        title = request.POST.get("title")
        price = request.POST.get("price")
        cate = request.POST.get("mcate")
        bigcate = request.POST.get("bigcate")
        smallcate = request.POST.get("smallcate")
        mtuo = request.POST.get("mtuo")
        tuone = request.POST.get("toone")
        result = request.POST.get("mresult")
        content = request.POST.get("content")

        try:
            bid = bigCate.objects.get(bcate_name = bigcate).id
            mm.m_bigcate_id = bid
        except:
            pass
        try:
            sid = smallCate.objects.get(scate_name = smallcate).id
            mm.m_smallcate_id = sid
        except:
            pass
        try:
            mtoid = Author.objects.get(scate_name = tuone).id
            mm.m_to_id = mtoid
        except:
            pass

        mm.m_name = title if title else mm.m_name
        mm.m_price = price if price else mm.m_price
        mm.m_content = content if content else mm.m_content
        mm.m_cate_xuorfu = cate if cate else mm.m_cate_xuorfu


        mm.m_tuoing = mtuo if mtuo else mm.m_tuoing
        mm.m_result = result if title else mm.m_result
        mm.save()

        return render_to_response("userone.html",{
            "name":name,
            "pwd":pwd,
            "author":author,
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "news_list":news_list,
            "message":mm,
            "moneyin":moneyin,
            "moneyout":moneyout,
            "mxuok":mxuok,
            "mfwok":mfwok,
            "mxu":mxu,
            "mfw":mfw,
            "mxuing":mxuing,
            "mfwing":mfwing
        })

    else:
        m = Message.objects.get(m_num=id)
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            author = Author.objects.get(author_name=name)
            return render_to_response("message.html", {
            "title":"",
            'name':name,
            'pwd':pwd,
            "author":author,
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "m":m,
            "news_list":news_list,
            "moneyin":moneyin,
            "moneyout":moneyout,
            "mxuok":mxuok,
            "mfwok":mfwok,
            "mxu":mxu,
            "mfw":mfw,
            "mxuing":mxuing,
            "mfwing":mfwing
            })
        except:
            return render_to_response("logre/login.html", {
                "error":"你还没有登录,请先登录",
            })


def user(request):
    hot_list = Message.objects.filter(m_tuoing="否").order_by("-m_seenum")[:6]
    news_list = bbs.objects.all().order_by("-bbs_time")[:6]
    blog_list = Blog.objects.all().order_by("-blog_time")[:6]
    try:
        jin_list = Message.objects.all()[:6]
        name = request.session["username"]
        xingqu = Author.objects.get(author_name=name).author_xingqu
        like_list = Message.objects.filter(m_bigcate__contains=xingqu) | Message.objects.filter(m_smallcate__contains=xingqu)
        like_list = like_list[:6]
    except:
        like_list = Message.objects.all()[:6]

    moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing=tongji.tongji(request)
    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        author = Author.objects.get(author_name=name)
        try:
            xuqiu_list = Message.objects.filter(m_from = name,m_cate_xuorfu="需求").order_by("-m_time")[:13]
            return render_to_response("user.html",{
                "name": name,
                "pwd": pwd,
                "email": author.author_eamil,
                "phone":author.author_phone,
                "qq":author.author_qq,
                "xuqiu_list": xuqiu_list,
                "color1":"#e54d4b",
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
		"news_list":news_list,
                "blog_list":blog_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
                })
        except:
            return render_to_response("user.html",{
                "name":name,
                "pwd":pwd,
                "email":author.author_eamil,
                "phone":author.author_phone,
                "qq":author.author_qq,
                "color1":"#e54d4b",
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
		"news_list":news_list,
                "blog_list":blog_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
                })
    except:
        return render_to_response("csmarket.html",{ })

def userFw(request):
    hot_list = Message.objects.filter(m_tuoing="否").order_by("-m_seenum")[:6]
    #jin_list = random.sample(Message.objects.all(),6)
    jin_list = Message.objects.all()[:6]
    news_list = bbs.objects.all().order_by("-bbs_time")[:6]
    blog_list = Blog.objects.all().order_by("-blog_time")[:6]
    try:
        name = request.session["username"]
        xingqu = Author.objects.get(author_name=name).author_xingqu
        like_list = Message.objects.filter(m_bigcate__contains=xingqu) | Message.objects.filter(m_smallcate__contains=xingqu)
        like_list = like_list[:6]
    except:
        like_list = Message.objects.all()[:6]
    moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing=tongji.tongji(request)

    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        author = Author.objects.get(author_name=name)
        try:
            fuwu_list = Message.objects.filter(m_from = name,m_cate_xuorfu="服务").order_by("-m_time")[:13]
            return render_to_response("user.html",{
                "name": name,
                "pwd": pwd,
                "email": author.author_eamil,
                "phone":author.author_phone,
                "qq":author.author_qq,
                "xuqiu_list": fuwu_list,
                "color2":"#e54d4b",
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
                "news_list":news_list,
                "blog_list":blog_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
                })
        except:
            return render_to_response("user.html",{
                "name":name,
                "pwd":pwd,
                "email":author.author_eamil,
                "phone":author.author_phone,
                "qq":author.author_qq,
                "color2":"#e54d4b",
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
                "news_list":news_list,
                "blog_list":blog_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
                })
    except:
        return render_to_response("user.html",{ })

def userOne(request,id):
    hot_list = Message.objects.filter(m_tuoing="否").order_by("-m_seenum")[:6]
    jin_list = Message.objects.all()[:6]
    news_list = bbs.objects.all().order_by("-bbs_time")[:6]
    blog_list = Blog.objects.all().order_by("-blog_time")[:6]
    moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing=tongji.tongji(request)

    try:
        name = request.session["username"]
        xingqu = Author.objects.get(author_name=name).author_xingqu
        like_list = Message.objects.filter(m_bigcate__contains=xingqu) | Message.objects.filter(m_smallcate__contains=xingqu)
        like_list = like_list[:6]
    except:
        like_list = Message.objects.all()[:6]

    message = Message.objects.get(m_num=id)

    new_seenum = message.m_seenum+1
    Message.objects.filter(m_num=id).update(m_seenum = new_seenum)

    try:
        name = request.session["username"]
        pwd = request.session["pwd"]
        author = Author.objects.get(author_name=name)

        return render_to_response("userone.html",{
            "name": name,
            "pwd": pwd,
            "author":author,
            "message": message,
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "news_list":news_list,
            "blog_list":blog_list,
            "moneyin":moneyin,
            "moneyout":moneyout,
            "mxuok":mxuok,
            "mfwok":mfwok,
            "mxu":mxu,
            "mfw":mfw,
            "mxuing":mxuing,
            "mfwing":mfwing
            })
    except:
        return render_to_response("userone.html",{
            "message": message,
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "news_list":news_list,
            "blog_list":blog_list,
        })

@csrf_exempt
def userAlter(request):
    hot_list = Message.objects.filter(m_tuoing="否").order_by("-m_seenum")[:6]
    #jin_list = random.sample(Message.objects.all(),6)
    news_list = bbs.objects.all().order_by("-bbs_time")[:6]
    jin_list = Message.objects.all()[:6]
    blog_list = Blog.objects.all().order_by("-blog_time")[:6]
    try:
        name = request.session["username"]
        xingqu = Author.objects.get(author_name=name).author_xingqu
        like_list = Message.objects.filter(m_bigcate__contains=xingqu) | Message.objects.filter(m_smallcate__contains=xingqu)
        like_list = like_list[:6]
    except:
        like_list = Message.objects.all()[:6]
    moneyin,moneyout,mxuok,mfwok,mxu,mfw,mxuing,mfwing=tongji.tongji(request)

    if request.method =="POST":
        f_name = request.POST.get("name")
        f_email = request.POST.get("email")
        f_phone = request.POST.get("phone")
        f_qq = request.POST.get("qq")
        f_newpwd = request.POST.get("newpwd")
        f_xingqu = request.POST.get("xingqu")

        o_name = request.session["username"]
        author = Author.objects.get(author_name=o_name)

        name = f_name if f_name else o_name
        email = f_email if f_email else author.author_eamil
        phone = f_phone if f_phone else author.author_phone
        qq = f_qq if f_qq else author.author_qq
        pwd = f_newpwd if f_newpwd else author.author_pwd
        xingqu = f_xingqu if f_xingqu else author.author_xingqu

        #将信息写入session表
        request.session["username"] = name
        request.session["pwd"] = pwd

        author.author_name = name
        author.author_eamil = email
        author.author_phone = phone
        author.author_qq = qq
        author.author_pwd = pwd
        author.author_xingqu = xingqu
        author.save()

        xuqiu_list = Message.objects.filter(m_from = name,m_cate_xuorfu="需求")[:10]
        return render_to_response("user.html",{
            "name": name,
            "pwd": pwd,
            "phone":phone,
            "qq":qq,
            "email":email,
            "xuqiu_list":xuqiu_list,
            "mess":"信息修改完成",
            "hot_list":hot_list,
            "like_list":like_list,
            "jin_list":jin_list,
            "news_list":news_list,
            "blog_list":blog_list,
            "moneyin":moneyin,
            "moneyout":moneyout,
            "mxuok":mxuok,
            "mfwok":mfwok,
            "mxu":mxu,
            "mfw":mfw,
            "mxuing":mxuing,
            "mfwing":mfwing
            })
    else:
        try:
            name = request.session["username"]
            pwd = request.session["pwd"]
            author = Author.objects.get(author_name=name)
            return render_to_response("useralter.html",{
                "name": name,
                "pwd": pwd,
                "author":author,
                "hot_list":hot_list,
                "like_list":like_list,
                "jin_list":jin_list,
                "news_list":news_list,
                "blog_list":blog_list,
                "moneyin":moneyin,
                "moneyout":moneyout,
                "mxuok":mxuok,
                "mfwok":mfwok,
                "mxu":mxu,
                "mfw":mfw,
                "mxuing":mxuing,
                "mfwing":mfwing
            })
        except:
            return render_to_response("useralter.html",{ })


def forall(request,id):
    try:
        mname = bigCate.objects.get(bcate_num=id).bcate_name
        mid = bigCate.objects.get(bcate_num=id).id
        message_list = Message.objects.filter(m_bigcate_id = mid)
    except:
        mname = smallCate.objects.get(scate_num=id).scate_name
        mid = smallCate.objects.get(scate_num=id).id
        message_list = Message.objects.filter(m_smallcate_id = mid)


    try:
       name = request.session["username"]
       return render_to_response("forall.html",{
            "name":name,
            "message_list":message_list,
        })
    except:
        return render_to_response("forall.html",{
            "message_list":message_list,
        })
