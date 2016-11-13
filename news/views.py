#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from news.models import news
# Create your views here.
def home(request):
    news_list = news.objects.all()
    count_news = len(news_list)
    return render_to_response("news.html",{
        "news_list":news_list,
        "count_news":count_news,
    })
