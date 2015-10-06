from django.shortcuts import render
from app.models import News, Admin
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
    return render(request, 'admin/pub_news.html', {

    })


# @csrf_exempt
# def admin_login(request):
#     username = request.POST['login']
#     password = request.POST['pwd']
#     print username, password
#     return HttpResponse("success")



# Create your views here.
