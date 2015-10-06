# coding=utf-8
from django.shortcuts import render
from app.models import News, Admin
import time
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache

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


def admin_news(request):
    news_info = {}
    innerhtml1 = ""
    innerhtml2 = "<option value='0'>请选择</option>"
    try:
        news_type = int(request.GET['news_type'])
    except:
        news_type = 0
    if news_type == 0:
        news_list = News.objects.all()[0:20]
    else:
        print "new_type", news_type
        if news_type < 10:
            print "big type"
            news_list = News.objects.filter(news_type__istartswith=news_type)
        else:
            news_list = News.objects.filter(news_type=news_type)

    print "news_list_len", len(news_list)
    if news_type < 10:
        first_type = news_type
        second_type = 0
    else:
        first_type = news_type / 10
        second_type = news_type % 10
    for news in news_list:
        user = news.news_author
        news_info[news] = user

    count = -1
    for first in first_tuple:
        count += 1
        if count == first_type:
            innerhtml1 += "<option selected='selected' value="
        else:
            innerhtml1 += "<option value="

        innerhtml1 += "'" + str(count) + "'>" + str(first) + "</option>"
    count = 0
    for i in second_dic[str(first_type)]:
        count += 1
        if count == second_type:
            innerhtml2 += "<option selected='selected' value="
        else:
            innerhtml2 += "<option value="
        innerhtml2 += "'" + str(count) + "'>" + str(i) + "</option>"
    # print innerhtml1
    # print innerhtml2
    # return HttpResponse(news_info.values())
    return render(request, 'admin/admin_news.html', {
        'news_info': news_info,
        'innerhtml1': innerhtml1,
        'innerhtml2': innerhtml2,
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

@csrf_exempt
def pub_news(request):
    news_content = request.POST['mycontent']
    news_title = request.POST['pubnews_title']
    dateString = request.POST['nowtime']
    first_type = int(request.POST['selType'])
    second_type = int(request.POST['selType2'])
    print first_type, second_type
    admin = Admin.objects.get(admin_id=1)

    new_news = News(
       news_title=news_title,
       news_type=first_type*10 + second_type,
       news_content=news_content,
       news_update_time=dateString,
       news_author=admin,
    )
    new_news.save()
    return HttpResponseRedirect('admin_news')


@csrf_exempt
def sel_change(request):
    first_type = request.GET['first']
    print first_type
    innerhtml = ""
    print innerhtml
    count = 0
    for i in second_dic[first_type]:
        count += 1
        innerhtml += "<option value="
        innerhtml += "'" + str(count) + "'>" + str(i) + "</option>"
    print innerhtml
    return HttpResponse(innerhtml)



# @csrf_exempt
# def admin_login(request):
#     username = request.POST['login']
#     password = request.POST['pwd']
#     print username, password
#     return HttpResponse("success")



# Create your views here.
