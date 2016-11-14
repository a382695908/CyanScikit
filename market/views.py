#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from market.models import wcate,example
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def home(request):
    wcate_list = wcate.objects.all()

    #example list
    example_list = example.objects.all()
    paginator = Paginator(example_list, 6)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        examples = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        examples = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        examples = paginator.page(paginator.num_pages)

    return render_to_response("maket.html",{
        "wcate_list":wcate_list,
        'examples': examples,
    })

def cate(request,num):
    #get all wcate
    wcate_list = wcate.objects.all()
    #get one wcate message
    ow_mess = wcate.objects.get(wcate_id=num)

    #get examples of the cate
    ex_list = example.objects.filter(ex_category__wcate_id=num)
    return render_to_response("maket_type.html",{
        "wcate_list": wcate_list,
        "ow_mess":ow_mess,
        "ex_list":ex_list,
    })

def oneex(request,exid):
    # get all wcate
    wcate_list = wcate.objects.all()
    # update seenum
    one = example.objects.get(ex_id=exid)
    one.ex_seenum = one.ex_seenum+1
    one.save()
    # get one example message
    oneex_mess = example.objects.get(ex_id=exid)
    return render_to_response("maket_one_mess.html",{
        "wcate_list": wcate_list,
        "oneex_mess":oneex_mess,
    })