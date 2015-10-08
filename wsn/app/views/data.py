#coding=utf-8
import sys
from app.models import Air, Water
from django.shortcuts import render
from django.http import HttpResponse
import random
import time

air_parameter = ["pm25", "cloud", "rain", "ziwai", "guang", "clouddir"]
air_parameter_data = {
    "pm25": {"name": "PM2.5", "unit": "(μg/立方米)"},
    "cloud": {"name": "风速",  "unit": "(m/s)"},
    "rain": {"name": "雨量", "unit": "(ms/平方米)）" },
    "ziwai": {"name": "紫外线指数", "unit": "(uw/平方厘米)"},
    "guang": {"name": "光量子", "unit": "(umol/m^2*s)"},
    "clouddir": {"name": "风向", "unit": "" }
}
cloud_dir = ["E", "ESE", "SE", "SSE", "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"]
cloud_dir_data = {
    "E": {"count": 0},
    "ESE": {"count": 0},
    "SE": {"count": 0},
    "SSE": {"count": 0},
    "S": {"count": 0},
    "SSW": {"count": 0},
    "SW": {"count": 0},
    "WSW": {"count": 0},
    "W": {"count": 0},
    "WNW": {"count": 0},
    "NW": {"count": 0},
    "NNW": {"count": 0},
    "N": {"count": 0}
}

def air(request):
    air_type = "pm25"
    try:
        air_type = request.GET['air_type']
    except:
        air_type = "pm25"
    data = []
    air_list = Air.objects.all()[0:30]
    air_type = str(air_type)
    main_count = 0
    for dir in cloud_dir:
        print dir
        print cloud_dir_data[dir]["count"]
        cloud_dir_data[dir]["count"] = 0
    # return HttpResponse(cloud_dir_data)

    for air in air_list:
        main_count += 1
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
            data.append(air.pm25)
            cloud_dir_data[air.clouddir]["count"] += 1

    print main_count
    cloud_dir_count_data = []
    for dir in cloud_dir:
        print cloud_dir_data[dir]["count"]
        count = {}
        count["name"] = dir
        count["y"] = cloud_dir_data[dir]["count"] / (main_count * 1.0)
        cloud_dir_count_data.append(count)
        # cloud_dir_count_data[dir] = cloud_dir_data[dir]["count"] / (main_count * 1.0)
        # print cloud_dir_count_data[dir]


    title = air_parameter_data[air_type]["name"]
    unit = air_parameter_data[air_type]["unit"]
    # return HttpResponse(cloud_dir_count_data)
    return render(request, 'air.html', {
        "data": data,
        "title": title,
        "unit": unit,
        "air_type": air_type,
        "cloud_dir_count_data": cloud_dir_count_data
        })

water_parameter = ["ph", "do", "turbidity", "water_level", "conductivity"]
water_parameter_data = {
    "ph": {"name": "酸碱度", "unit": ""},
    "do": {"name": "溶解氧", "unit": "mg/L"},
    "turbidity": {"name": "浊度", "unit": "FTU"},
    "water_level": {"name": "水位", "unit": "米"},
    "conductivity": {"name": "电导率", "unit": "s/cm"},
}
def water(request):
    water_type = "ph"
    try:
        water_type = request.GET("water_type")
    except:
        pass

    water_list = Water.objects.all()[0:30]
    water_unit = water_parameter_data[water_type]["unit"]
    water_title = water_parameter_data[water_type]["name"]
    # print water_unit, water_title
    test = []
    water_data = []
    for water in water_list:
        tmp_dic = {}
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        data_time = water.time
        data_time_format = data_time.strftime(ISOTIMEFORMAT)
        timeArray = time.strptime(data_time_format, "%Y-%m-%d %H:%M:%S")
        seconds = int(time.mktime(timeArray))
        tmp_dic["x"] = str(seconds * 1000)
        tmp_dic["y"] = float(water.ph)
        water_data.append(tmp_dic)
    print water_data
    return render(request, "water.html", {
        "water_unit": water_unit,
        "water_title": water_title,
        "water_data": water_data,
    })


# Create your views here.

