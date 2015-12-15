from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


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
