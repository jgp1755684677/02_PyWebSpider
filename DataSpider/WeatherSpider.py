import urllib.request as req
import re


# 定义爬取weather.com.cn网站的爬虫类
class WeatherSpider:
    # 定义存储字符串的数组
    _table = []

    # WeatherSpider初始化函数，并通过该函数获取url网页内容
    def __init__(self, url):
        # 打开url链接
        web = req.urlopen(url)
        # 读取网页的数据
        html = web.read()
        # 将byte类型数据转换成字符串
        html = html.decode('utf-8')
        # 将字符串数据存储到私有变量html中
        self._html = html
        # 获取<div class="rank"></div>标签里面的内容
        # 定义匹配字符标签
        label = r'<div class="rank">(.*?)</div>'
        # 获取所有符合条件的字符串，并保存到table中
        table = re.findall(label, self._html, re.S)
        # 定义匹配字符标签
        label = r'<ul(.*?)</ul>'
        # 获取所有符合条件的字符串，并保存到table中
        table = re.findall(label, table[0], re.S)
        # 将获取的字符串复制到私有数组table中
        self._table = table

    def get_high_temp(self):
        # 定义获取排名的标签
        sort_label = r'<span class="ord"><i>(.*?)</i></span>'
        # 获取排名数组
        sort = re.findall(sort_label, self._table[0], re.S)
        # 定义获取城市标签
        city_label = r'<span class="city"><a(.*?)</span>'
        # 获取城市数组
        city = re.findall(city_label, self._table[0], re.S)
        # 剔除每个城市中的超链接
        for i in range(len(city)):
            city[i] = re.findall(r'target="_blank">(.*?)</a>', city[i], re.S)[0]
        # 定义获取省份的标签
        prov_label = r'<span class="prov"><a(.*?)</span>'
        # 获取省份数组
        prov = re.findall(prov_label, self._table[0], re.S)
        # 剔除每个省份中的超链接
        for i in range(len(city)):
            prov[i] = re.findall(r'target="_blank">(.*?)</a>', prov[i], re.S)[0]
        # 定义获取最高温的标签
        high_temp_label = r'<span class="wd">(.*?)℃<span'
        # 获取最高气温数组
        high_temp = re.findall(high_temp_label, self._table[0], re.S)
        # 定义数组存储四个数组
        high_temp_array = []
        # 向数组中添加值
        for i in range(len(sort)):
            temp = [sort[i], city[i], prov[i], high_temp[i]]
            high_temp_array.append(temp)
        # 返回结果数组
        return high_temp_array

    def get_differ_temp(self):
        # 定义获取排名的标签
        sort_label = r'<span class="ord"><i>(.*?)</i></span>'
        # 获取排名数组
        sort = re.findall(sort_label, self._table[1], re.S)
        # 定义获取城市标签
        city_label = r'<span class="city"><a(.*?)</span>'
        # 获取城市数组
        city = re.findall(city_label, self._table[1], re.S)
        # 剔除每个城市中的超链接
        for i in range(len(city)):
            city[i] = re.findall(r'target="_blank">(.*?)</a>', city[i], re.S)[0]
        # 定义获取省份的标签
        prov_label = r'<span class="prov"><a(.*?)</span>'
        # 获取省份数组
        prov = re.findall(prov_label, self._table[1], re.S)
        # 剔除每个省份中的超链接
        for i in range(len(city)):
            prov[i] = re.findall(r'target="_blank">(.*?)</a>', prov[i], re.S)[0]
        # 定义获取最高温的标签
        differ_temp_label = r'<span class="wd">(.*?)℃</span>'
        # 获取最高气温数组
        differ_temp = re.findall(differ_temp_label, self._table[1], re.S)
        # 定义数组存储四个数组
        differ_temp_array = []
        # 向数组中添加值
        for i in range(len(sort)):
            temp = [sort[i], city[i], prov[i], differ_temp[i]]
            differ_temp_array.append(temp)
        # 返回结果数组
        return differ_temp_array

    def get_precipitation(self):
        # 定义获取排名的标签
        sort_label = r'<span class="ord"><i>(.*?)</i></span>'
        # 获取排名数组
        sort = re.findall(sort_label, self._table[2], re.S)
        # 定义获取城市标签
        city_label = r'<span class="city"><a(.*?)</span>'
        # 获取城市数组
        city = re.findall(city_label, self._table[2], re.S)
        # 剔除每个城市中的超链接
        for i in range(len(city)):
            city[i] = re.findall(r'target="_blank">(.*?)</a>', city[i], re.S)[0]
        # 定义获取省份的标签
        prov_label = r'<span class="prov"><a(.*?)</span>'
        # 获取省份数组
        prov = re.findall(prov_label, self._table[2], re.S)
        # 剔除每个省份中的超链接
        for i in range(len(city)):
            prov[i] = re.findall(r'target="_blank">(.*?)</a>', prov[i], re.S)[0]
        # 定义获取最高温的标签
        precipitation_label = r'<span class="wd">(.*?)mm</span>'
        # 获取最高气温数组
        precipitation = re.findall(precipitation_label, self._table[2], re.S)
        # 定义数组存储四个数组
        precipitation_array = []
        # 向数组中添加值
        for i in range(len(sort)):
            temp = [sort[i], city[i], prov[i], precipitation[i]]
            precipitation_array.append(temp)
        # 返回结果数组
        return precipitation_array


if __name__ == '__main__':
    # 定义爬虫目标网页的Url
    url = 'http://www.weather.com.cn/'
    # 创建爬虫对象
    data = WeatherSpider(url)
    # 获取最高气温
    high_temp = data.get_high_temp()
    # 打印最高气温
    print(high_temp)
    # 获取昼夜温差
    differ_temp = data.get_differ_temp()
    # 打印昼夜温差
    print(differ_temp)
    # 获取降水量
    precipitation = data.get_precipitation()
    # 打印降水量
    print(precipitation)
