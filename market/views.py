#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from market.models import wcate,example
# Create your views here.
def home(request):
    wcate_list = wcate.objects.all()
    return render_to_response("maket.html",{
        "wcate_list":wcate_list,
    })

def cate(request,num):
    #get all wcate
    wcate_list = wcate.objects.all()
    #get one wcate message
    ow_mess = wcate.objects.get(wcate_id=num)
    return render_to_response("maket_type.html",{
        "wcate_list": wcate_list,
        "ow_mess":ow_mess,
    })