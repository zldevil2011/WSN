from django.shortcuts import render
from app.models import News, Admin
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache


def admin_news(request):
    news_list = News.objects.all()
    authors = []
    for news in news_list:
        user = news.news_author
        authors.append(user)
    # return HttpResponse("AK47")
    return render(request, 'admin/admin_news.html', {
        'news_list': news_list,
        'authors': authors,
    })


# @csrf_exempt
# def admin_login(request):
#     username = request.POST['login']
#     password = request.POST['pwd']
#     print username, password
#     return HttpResponse("success")



# Create your views here.
