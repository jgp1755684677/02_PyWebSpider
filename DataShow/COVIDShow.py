# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from DataTrans.COVIDTrans import COVIDTrans


def cov_show(path):
    # 定义时间滚动栏标题
    title = ['现存确诊人数', '累计确诊人数', '累计治愈人数', '累计死亡人数']
    # 定义查询字段
    field = ['current_count', 'ncov_count', 'cured_count', 'dead_count']
    # 定义分段显示色段方案
    colormap = [[{"max": 90000, "min": 10001, "label": ">10000", "color": "#FF0000"},
                 {"max": 10000, "min": 1000, "label": "1000-10000", "color": "#FF2D2D"},
                 {"max": 999, "min": 500, "label": "500-999", "color": "#FF5151"},
                 {"max": 499, "min": 100, "label": "100-499", "color": "#ff7575"},
                 {"max": 99, "min": 10, "label": "10-99", "color": "#FF9797"},
                 {"max": 9, "min": 1, "label": "1-9", "color": "#FFB5B5"},
                 {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"}],
                [{"max": 90000, "min": 10001, "label": ">10000", "color": "#5E005E"},
                 {"max": 10000, "min": 1000, "label": "1000-10000", "color": "#FF00FF"},
                 {"max": 999, "min": 500, "label": "500-999", "color": "#FF44FF"},
                 {"max": 499, "min": 100, "label": "100-499", "color": "#FF77FF"},
                 {"max": 99, "min": 10, "label": "10-99", "color": "#FF8EFF"},
                 {"max": 9, "min": 1, "label": "1-9", "color": "#FFD0FF"},
                 {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"}],
                [{"max": 90000, "min": 10001, "label": ">10000", "color": "#006030"},
                 {"max": 10000, "min": 1000, "label": "1000-10000", "color": "#019858"},
                 {"max": 999, "min": 500, "label": "500-999", "color": "#02C874"},
                 {"max": 499, "min": 100, "label": "100-499", "color": "#02F78E"},
                 {"max": 99, "min": 10, "label": "10-99", "color": "#4EFEB3"},
                 {"max": 9, "min": 1, "label": "1-9", "color": "#96FED1"},
                 {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"}],
                [{"max": 10000, "min": 1000, "label": "1000-10000", "color": "#408080"},
                 {"max": 999, "min": 500, "label": "500-999", "color": "#5CADAD"},
                 {"max": 499, "min": 100, "label": "100-499", "color": "#81C0C0"},
                 {"max": 99, "min": 10, "label": "10-99", "color": "#A3D1D1"},
                 {"max": 9, "min": 1, "label": "1-9", "color": "#C4E1E1"},
                 {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"}]
                ]
    # 创建时间线对象
    tl = Timeline()
    for i in range(4):
        # 获得数据
        data = COVIDTrans().get_data(field[i])
        # 定义地图标题
        map_title = "2020年3月15日新型肺炎" + title[i] + "全国分布图"
        # 创建地图对象
        map0 = Map()
        # 向地图中添加数据
        map0.add("", data, "china")
        # 创建地图显示方式
        map0.set_global_opts(title_opts=opts.TitleOpts(title=map_title,), visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=colormap[i]))
        # 将地图添加到时间线中
        tl.add(map0, title[i])
    # 生成html文件
    tl.render(path)


if __name__ == '__main__':
    # 绘制图表
    cov_show("../Results/COVID.html")
