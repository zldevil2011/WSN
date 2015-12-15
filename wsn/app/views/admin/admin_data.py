# coding=utf-8
from django.shortcuts import render
from app.models import News, Admin, Air, Water
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


@csrf_exempt
def admin_data(request):
    # try:
    #     user = Admin.objects.get(admin_username = request.session["admin_username"])
    # except:
    #     return HttpResponseRedirect("/wsn_admin/index/")
    data_type = request.GET["data_type"]
    if data_type == "air":
        air_list = Air.objects.all()
        return render(request, "admin/admin_data_air.html", {
            "air_list" : air_list,
        })
    elif data_type == "water":
        water_list = Water.objects.all()
        return render(request, "admin/admin_data_water.html", {
            "water_list" : water_list
        })
    else:
        return  HttpResponse("Sorry 该类数据不存在")


@csrf_exempt
def admin_data_upload(request):
    print "come in"
    try:
        data_type = request.POST['data_type']
        print data_type
    except:
        print "get Failed"
    try:
        data_file = request.FILES['data_file']
        print data_file
    except:
        print "get FILE FAILED"
    print "JuST  Here"
    return HttpResponse("success")
# Create your views here.
