#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from item.models import item
# Create your views here.

def home(request):
    item_list = item.objects.all()
    paginator = Paginator(item_list, 6)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        all_item = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        all_item = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        all_item = paginator.page(paginator.num_pages)

    return render(request, 'item.html', {
        'all_item': all_item,
    })

def one(request,itemid):
    item_mess = item.objects.get(item_id=itemid)
    return render_to_response("item_one_page.html",{
        "item_mess":item_mess,
    })