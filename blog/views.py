#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import blog,cate
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

def one(request,id):
    blog_mess = blog.objects.get(blog_id=id)
    #update seenum
    blog_mess.blog_seenum = blog_mess.blog_seenum + 1
    blog_mess.save()
    return render_to_response("blog_one_page.html",{
        "blog_mess":blog_mess,
        "cates": getcate(),
        "hot_list":gethot(),
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