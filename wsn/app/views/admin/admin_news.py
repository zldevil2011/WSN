# coding=utf-8
from django.shortcuts import render
from app.models import News, Admin
import time
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache


def admin_news(request):
    news_info = {}

    news_list = News.objects.all()

    for news in news_list:
        user = news.news_author
        news_info[news] = user
    # return HttpResponse(news_info.values())
    return render(request, 'admin/admin_news.html', {
        'news_info': news_info
    })


def pub_news_page(request):
    # innerhtml = "<option value= '0'>请选择</option>"
    # innerhtml += newsService.get_first_innerhtml()
    ISOTIMEFORMAT = '%Y-%m-%d %X'
    currentTime = time.strftime(ISOTIMEFORMAT, time.localtime())
    # print innerhtml
    return render(request, 'admin/pub_news.html', {
        # "innerhtml1": innerhtml,
        "nowtime": currentTime
    })


# @csrf_exempt
# def admin_login(request):
#     username = request.POST['login']
#     password = request.POST['pwd']
#     print username, password
#     return HttpResponse("success")



# Create your views here.
