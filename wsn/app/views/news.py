#coding=utf-8
import sys
from app.models import News
from django.shortcuts import render
from django.http import HttpResponse
first_tuple = ["请选择", "基地概况", "新闻公告", "观测设备", "服务流程", "政策法规", "常用下载","测试专用" ]
second_dic = {
    '0': {},
    '1': {"基地介绍"},
    '2': {"动态新闻", "通知公告"},
    '3': {"观测设备" },
    '4': {"服务流程" },
    '5': {"国家标准", "行业标准", "国际标准", "其他标准"},
    '6': {"常用下载"},
    '7': {"测试页面"},
}

def news_list(request):
    try:
        news_type = int(request.GET['news_type'])
    except:
        news_type = 0
    page_title = ""
    if news_type == 0:
        news_list = News.objects.all()[0:20]
        tmp_list = news_list[0:5]
        page_title = "所有新闻"
    else:
        if news_type < 10:
            news_list = News.objects.filter(news_type__istartswith=news_type)[0:20]
            tmp_list = news_list[0:5]
            page_title = first_tuple[news_type]
        else:
            news_list = News.objects.filter(news_type=news_type)
            tmp_list = news_list[0:5]
            count = 0
            for i in second_dic[str(news_type / 10)]:
                count += 1
                if count == news_type % 10:
                    page_title = str(i)
                    print i
                    break

    for news in news_list:
        news.news_update_time = news.news_update_time[2:16]
    return render(request, "news_list.html", {
        "news_list": news_list,
        "tmp_list": tmp_list,
        "page_title": page_title,
    })


def news_detail(requst, news_id):
    try:
        news = News.objects.get(news_id=news_id)
    except News.DoesNotExist:
        return HttpResponse("Sorry, Page not found")
    tmp_list = News.objects.all()[0:5]
    return render(requst, 'news.html', {
        'news': news,
        'tmp_list': tmp_list
    })

# Create your views here.
