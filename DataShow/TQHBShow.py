# -*- coding: utf-8 -*-
from pyecharts import options as opts
from pyecharts.charts import Map, Timeline
from DataTrans.TQHBTrans import TQHBTrans


#
def temp_show(field, name, path):
    # 定义时间滚动栏标题
    title = TQHBTrans().get_date()
    print(title)
    # 创建时间线对象
    tl = Timeline()
    for i in range(len(title)):
        print(i)
        data = TQHBTrans().get_temp(title[i], field)
        # 定义地图标题
        map_title = str(title[i])[0:4] + "年" + str(title[i])[4:6] + "月" + str(title[i])[6:8] + "日全国各省会" + name + "分布图"
        # 创建地图对象
        map0 = Map()
        # 向地图中添加数据
        map0.add("", data, "china")
        # 创建地图显示方式
        map0.set_global_opts(title_opts=opts.TitleOpts(title=map_title, ),
                             visualmap_opts=opts.VisualMapOpts(is_piecewise=True, pieces=[
                                 {"max": 40, "min": 31, "label": "31-40℃", "color": "#FF8000"},
                                 {"max": 30, "min": 21, "label": "21-30℃", "color": "#FFBB77"},
                                 {"max": 20, "min": 11, "label": "11-20℃", "color": "#FFDCB9"},
                                 {"max": 10, "min": 1, "label": "1-10℃", "color": "#FFEEDD"},
                                 {"max": 0, "min": -10, "label": "-10-0℃", "color": "#C4E1FF"},
                                 {"max": -11, "min": -20, "label": "-20--11℃", "color": "#66B3FF"},
                                 {"max": -21, "min": -30, "label": "-30--21℃", "color": "#2894FF"}]))
        # 将地图添加到时间线中
        tl.add(map0, title[i])
    # 生成html文件
    tl.render(path)


if __name__ == '__main__':
    temp_show("low_temp", "最低气温", "../Results/TQHB.html")
