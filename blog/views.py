#-*-coding:utf-8-*-
from django.shortcuts import render,render_to_response

# Create your views here.
def home(request):
    return render_to_response("blog.html",{

    })

def one(request):
    return render_to_response("blog_one_page.html",{

    })