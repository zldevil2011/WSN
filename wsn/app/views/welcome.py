from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache


def welcome(request):
    try:
        wel = request.POST['wel']
    except:
        wel = "welcome WSN"
    return render(request, 'welcome.html', {})


# Create your views here.
