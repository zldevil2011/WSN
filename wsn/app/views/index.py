from django.shortcuts import render
from app.models import News
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache


def index(request):
    notice_list = News.objects.filter(news_type=22)[0:10]
    news_list = News.objects.filter(news_type=21)[0:10]

    return render(request, 'index.html', {
        'notice_list': notice_list,
        'news_list': news_list
    })


# Create your views here.
