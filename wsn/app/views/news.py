#coding=utf-8
import sys
from app.models import News
from django.shortcuts import render
from django.http import HttpResponse


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
