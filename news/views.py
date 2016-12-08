#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from news.models import news
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    news_list = news.objects.all().order_by("-news_time")
    paginator = Paginator(news_list, 12)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_news = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {
        'all_news': all_news,
        "len_list":range(1,paginator.num_pages ),
    })

def one(request,id):
    news_mess = news.objects.get(news_id=id)
    #update seenum
    news_mess.news_seenum = news_mess.news_seenum + 1
    news_mess.save()
    return  render_to_response("news_one.html",{
        "news_mess":news_mess,
    })
