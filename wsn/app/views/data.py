#coding=utf-8
import sys
from app.models import News, Air
from django.shortcuts import render
from django.http import HttpResponse

air_parameter = ["pm25", "cloud", "rain", "ziwai", "guang", "clouddir"]
air_parameter_data = {
    "pm25": {
        "name": "PM2.5",
        "unit": "(μg/立方米)"
    },
    "cloud": {
        "name": "风速",
        "unit": "(m/s)"
    },
    "rain": {
        "name": "雨量",
        "unit": "(ms/平方米)）"
    },
    "ziwai": {
        "name": "紫外线指数",
        "unit": "(uw/平方厘米)"
    },
    "guang": {
        "name": "光量子",
        "unit": "(umol/m^2*s)"
    },
    "clouddir": {
        "name": "风向",
        "unit": ""
    }
}
def air(request):
    air_type = "pm25"
    try:
        air_type = request.GET['air_type']
    except:
        air_type = "pm25"

    # data, title, danwei
    data = []
    air_list = Air.objects.all()[0:24]
    air_type = str(air_type)
    for air in air_list:
        if air_type == "pm25":
            data.append(air.pm25)
        elif air_type == "cloud":
            data.append(air.cloud)
        elif air_type == "rain":
            data.append(air.rain)
        elif air_type == "ziwai":
            data.append(air.ziwai)
        elif air_type == "guang":
            data.append(air.guang)
        elif air_type == "clouddir":
            data.append(air.clouddir)
    title = air_parameter_data[air_type]["name"]
    unit = air_parameter_data[air_type]["unit"]
    return render(request, 'air.html', {
        "data": data,
        "title": title,
        "unit": unit,
        "air_type": air_type,
        })

# Create your views here.
