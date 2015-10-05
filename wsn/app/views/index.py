from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache


def index(request):
    return render(request, 'index.html', {
        'notice_list': {},
        'news_list': {}
    })


# Create your views here.
