#coding=utf-8
import sys
from app.models import News, Water, Air
from django.shortcuts import render
from django.http import HttpResponse
import xlwt


air_parameter = ["pm25", "cloud", "rain", "ziwai", "guang", "clouddir"]
air_parameter_data = {
    "pm25": {"name": "PM2.5", "unit": "(μg/立方米)"},
    "cloud": {"name": "风速",  "unit": "(m/s)"},
    "rain": {"name": "雨量", "unit": "(ms/平方米)）" },
    "ziwai": {"name": "紫外线指数", "unit": "(uw/平方厘米)"},
    "guang": {"name": "光量子", "unit": "(umol/m^2*s)"},
    "clouddir": {"name": "风向", "unit": "" }
}
water_parameter = ["ph", "do", "turbidity", "water_level", "conductivity"]
water_parameter_data = {
    "ph": {"name": "酸碱度", "unit": ""},
    "do": {"name": "溶解氧", "unit": "(mg/L)"},
    "turbidity": {"name": "浊度", "unit": "(FTU)"},
    "water_level": {"name": "水位", "unit": "(米)"},
    "conductivity": {"name": "电导率", "unit": "(s/cm)"},
}
def get_excel(request):
    data_type = ""
    try:
        data_type = request.GET['data_type']
    except:
        data_type = "air"
    print "data_type", data_type
    wb =xlwt.Workbook(encoding='utf8')
    ws = wb.add_sheet('Sheetname')
    ws.write(0, 0, "采集时间", style=xlwt.Style.default_style)
    if data_type == "air":
        data_list = Air.objects.all()[0:100]
        for index, type in enumerate(air_parameter):
            ws.write(0, index + 1, air_parameter_data[type]["name"] +
                     air_parameter_data[type]["unit"], style=xlwt.Style.default_style)
        sum = [0, 0, 0, 0, 0, 0]
        max_data = [-9999, -9999, -9999,-9999, -9999, -9999]
        min_data = [9999, 9999, 9999,9999, 9999, 9999]
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        count = 1
        for data in data_list:
            ws.write(count, 0, data.time.strftime(ISOTIMEFORMAT), style=xlwt.Style.default_style)
            ws.write(count, 1, data.pm25, style=xlwt.Style.default_style)
            ws.write(count, 2, data.cloud, style=xlwt.Style.default_style)
            ws.write(count, 3, data.rain, style=xlwt.Style.default_style)
            ws.write(count, 4, data.ziwai, style=xlwt.Style.default_style)
            ws.write(count, 5, data.guang, style=xlwt.Style.default_style)
            ws.write(count, 6, data.clouddir, style=xlwt.Style.default_style)
            sum[1] += data.pm25
            if float(data.pm25) > max_data[1]:
                max_data[1] = float(data.pm25)
            if data.pm25 < min_data[1]:
                min_data[1] = data.pm25
            sum[2] += data.cloud
            if data.cloud > max_data[2]:
                max_data[2] = data.cloud
            if data.cloud < min_data[2]:
                min_data[2] = data.cloud
            sum[3] += data.rain
            if data.rain > max_data[3]:
                max_data[3] = data.rain
            if data.rain < min_data[3]:
                min_data[3] = data.rain
            sum[4] += data.ziwai
            if data.ziwai > max_data[4]:
                max_data[4] = data.ziwai
            if data.ziwai < min_data[4]:
                min_data[4] = data.ziwai
            sum[5] += data.guang
            if data.guang > max_data[5]:
                max_data[5] = data.guang
            if data.guang < min_data[5]:
                min_data[5] = data.guang
            count += 1
        ws.write(count, 0, "最大值", style=xlwt.Style.default_style)
        for i in range(1, 6):
            ws.write(count, i, max_data[i], style=xlwt.Style.default_style)
        count += 1
        ws.write(count, 0, "最小值", style=xlwt.Style.default_style)
        for i in range(1, 6):
            ws.write(count, i, min_data[i], style=xlwt.Style.default_style)
        count += 1
        ws.write(count, 0, "平均值", style=xlwt.Style.default_style)
        for i in range(1, 6):
            ws.write(count, i, sum[i]/float(len(data_list)), style=xlwt.Style.default_style)
        count += 1
    elif data_type == "water":
        data_list = Water.objects.all()[0:100]
        for index, type in enumerate(water_parameter):
            ws.write(0, index + 1, water_parameter_data[type]["name"] +
                     water_parameter_data[type]["unit"], style=xlwt.Style.default_style)
        sum = [0, 0, 0, 0, 0, 0]
        max_data = [-9999, -9999, -9999,-9999, -9999, -9999]
        min_data = [9999, 9999, 9999,9999, 9999, 9999]
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        count = 1
        for data in data_list:
            ws.write(count, 0, data.time.strftime(ISOTIMEFORMAT), style=xlwt.Style.default_style)
            ws.write(count, 1, data.ph, style=xlwt.Style.default_style)
            ws.write(count, 2, data.do, style=xlwt.Style.default_style)
            ws.write(count, 3, data.turbidity, style=xlwt.Style.default_style)
            ws.write(count, 4, data.water_level, style=xlwt.Style.default_style)
            ws.write(count, 5, data.conductivity, style=xlwt.Style.default_style)
            sum[1] += data.ph
            if float(data.ph) > max_data[1]:
                max_data[1] = float(data.ph)
            if data.ph < min_data[1]:
                min_data[1] = data.ph
            sum[2] += data.do
            if data.do > max_data[2]:
                max_data[2] = data.do
            if data.do < min_data[2]:
                min_data[2] = data.do
            sum[3] += data.turbidity
            if data.turbidity > max_data[3]:
                max_data[3] = data.turbidity
            if data.turbidity < min_data[3]:
                min_data[3] = data.turbidity
            sum[4] += data.water_level
            if data.water_level > max_data[4]:
                max_data[4] = data.water_level
            if data.water_level < min_data[4]:
                min_data[4] = data.water_level
            sum[5] += data.conductivity
            if data.conductivity > max_data[5]:
                max_data[5] = data.conductivity
            if data.conductivity < min_data[5]:
                min_data[5] = data.conductivity
            count += 1
        ws.write(count, 0, "最大值", style=xlwt.Style.default_style)
        for i in range(1, 6):
            ws.write(count, i, max_data[i], style=xlwt.Style.default_style)
        count += 1
        ws.write(count, 0, "最小值", style=xlwt.Style.default_style)
        for i in range(1, 6):
            ws.write(count, i, min_data[i], style=xlwt.Style.default_style)
        count += 1
        ws.write(count, 0, "平均值", style=xlwt.Style.default_style)
        for i in range(1, 6):
            ws.write(count, i, sum[i]/float(len(data_list)), style=xlwt.Style.default_style)
        count += 1


    response = HttpResponse(content_type="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=data.xls'
    wb.save(response)
    return response


# Create your views here.
