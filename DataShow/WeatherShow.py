# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Bar, Timeline
from DataTrans.WeatherTrans import WeatherTrans


# 展示绘制天气状况柱状统计图
def weather_show(path):
    # 定义时间线标题
    title = ["最高气温", "昼夜温差", "降水量"]
    # 定义查询字段
    field = ["high_temp", "differ_temp", "precipitation"]
    # 定义标记单位
    remarks = ["温度(℃)", "温度(℃)", "降水量(mm)"]
    # 定义时间线对象
    tl = Timeline()
    for i in range(3):
        # 查询数据
        name, value = WeatherTrans().get_data(field[i], field[i])
        # 统计表标题
        bar_title = "2020年3月15日全国" + title[i] + "Top 10 城市"
        # 定义柱状图对象
        bar = Bar()
        # 添加横坐标
        bar.add_xaxis(name)
        # 添加纵坐标
        bar.add_yaxis(remarks[i], value, label_opts=opts.LabelOpts(position="right"))
        # 绘制横向统计图
        bar.reversal_axis()
        # 添加标题
        bar.set_global_opts(title_opts=opts.TitleOpts(bar_title))
        # 将统计图添加到时间线中
        tl.add(bar, title[i])
    # 生成html文件
    tl.render(path)


if __name__ == '__main__':
    weather_show("../Results/Weather.html")
