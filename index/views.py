#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response

from market.models import wcate,example
from news.models import news
# Create your views here.
def home(request):
    wcate_list = wcate.objects.all()
    news_list = news.objects.all()[:5]
    return render_to_response("index.html",{
        "wcate_list":wcate_list,
        "news_list":news_list,
    })

def getweibo(request):
    return render_to_response("weibo.html",{})