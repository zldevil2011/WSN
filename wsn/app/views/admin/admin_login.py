from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import cache
from django.views.decorators.cache import never_cache


def admin_index(request):
    return render(request, 'admin/admin_login.html', {
    })


@csrf_exempt
def admin_login(request):
    username = request.POST['login']
    password = request.POST['pwd']
    print username, password
    return HttpResponse("success")



# Create your views here.
