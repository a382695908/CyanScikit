from django.http import HttpResponseRedirect

def index(request):
    return HttpResponseRedirect("/index/home")